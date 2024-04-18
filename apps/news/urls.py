from django.urls import path

from apps.news import views

app_name = "news"

urlpatterns = [
    path("", views.ArticlesView.as_view(), name="index"),
    path("save", views.SaveArticleView.as_view(), name="save_article"),
    path("remove", views.remove_saved_article, name="remove_article"),
]
