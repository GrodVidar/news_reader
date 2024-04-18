import uuid

from django.core import serializers
from django.forms.models import model_to_dict
from django.test import Client, TestCase
from django.urls import reverse

from .factories import ArticleFactory, SavedArticleFactory, SourceFactory


class ArticleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_id = uuid.uuid4()
        self.article = ArticleFactory()
        self.saved_articles = SavedArticleFactory(user_id=self.user_id)
        self.client.cookies["user_id"] = self.user_id

    def test_save_article(self):
        article_to_save = {
            "csrfmiddlewaretoken": "",
            "source.source_id": self.article.source.source_id,
            "source.name": self.article.source.name,
            "author": self.article.author,
            "title": self.article.title,
            "description": self.article.description,
            "url": self.article.url,
            "urlToImage": self.article.urlToImage,
            "publishedAt": self.article.publishedAt,
            "content": self.article.content,
            "category": self.article.category,
        }
        response = self.client.post(reverse("news:save_article"), article_to_save)
        self.assertEqual(response.status_code, 200)

        self.assertIn(self.article, self.saved_articles.articles.all())

    def test_remove_article(self):
        response = self.client.post(
            reverse("news:remove_article"), {"article_id": self.article.pk}
        )
        self.assertEqual(response.status_code, 200)

        self.assertNotIn(self.article, self.saved_articles.articles.all())
