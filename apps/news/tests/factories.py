import uuid

from factory import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ..models import Article, SavedArticle, Source

faker = Faker()


class SourceFactory(DjangoModelFactory):
    class Meta:
        model = Source


class ArticleFactory(DjangoModelFactory):
    source = SubFactory(SourceFactory)
    publishedAt = faker.past_datetime()

    class Meta:
        model = Article


class SavedArticleFactory(DjangoModelFactory):
    user_id = LazyAttribute(lambda x: uuid.uuid4())

    class Meta:
        model = SavedArticle
