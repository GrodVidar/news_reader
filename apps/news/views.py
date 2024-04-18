import uuid

from django.conf import settings
from django.shortcuts import render
from django.views import generic
from newsapi import NewsApiClient

from apps.news.models import Article, SavedArticle, Source


def create_model_instances(data, category):
    instances = []
    for item in data:
        if item["title"] == "[Removed]":
            continue
        source = Source(**item.pop("source"))
        instances.append(Article(source=source, category=category, **item))
    return instances


class ArticlesView(generic.ListView):
    model = Article
    template_name = "news/articles.html"
    context_object_name = "articles"

    QUERY_DATA = [
        {"q": "ai", "category": "ai"},
        {"q": "apple", "category": "apple"},
        {"country": "se", "category": "sweden"},
    ]

    def render_to_response(self, context, **response_kwargs):
        response = super(ArticlesView, self).render_to_response(
            context, **response_kwargs
        )
        if not self.request.COOKIES.get("user_id"):
            response.set_cookie("user_id", uuid.uuid4())
        return response

    def get_queryset(self):
        user_id = self.request.COOKIES.get("user_id")
        if user_id:
            if SavedArticle.objects.filter(user_id=user_id).exists():
                return (
                    SavedArticle.objects.filter(user_id=user_id).first().articles.all()
                )
        return SavedArticle.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
        api_data = {}
        for query_data in self.QUERY_DATA:
            query = {k: v for k, v in query_data.items() if k != "category"}
            response = newsapi.get_top_headlines(**query)
            print(response)
            if response["status"] == "ok":
                api_data[query_data["category"]] = create_model_instances(
                    response["articles"], query_data["category"]
                )
        context["api_data"] = api_data
        return context


class SaveArticleView(generic.View):
    def post(self, request, *args, **kwargs):
        user_id = self.request.COOKIES.get("user_id")
        if user_id:
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            source = {
                "source_id": data.pop("source.source_id"),
                "name": data.pop("source.name"),
            }
            source, _ = Source.objects.get_or_create(**source)
            article, _ = Article.objects.get_or_create(source=source, **data)
            saved_article, _ = SavedArticle.objects.get_or_create(user_id=user_id)
            saved_article.articles.add(article)
        return saved_articles_view(request)


def saved_articles_view(request):
    user_id = request.COOKIES.get("user_id")
    context = {}
    if user_id:
        context["articles"] = (
            SavedArticle.objects.filter(user_id=user_id).first().articles.all()
        )
    return render(request, "news/partial/saved_articles.html", context=context)


def remove_saved_article(request):
    if request.method == "POST":
        try:
            article_id = request.POST.dict()["article_id"]
            user_id = request.COOKIES.get("user_id")
            if user_id:
                saved_articles = SavedArticle.objects.get(user_id=user_id)
                saved_articles.articles.remove(article_id)
        finally:
            return saved_articles_view(request)
