from django.db import models


class Source(models.Model):
    source_id = models.CharField(max_length=255, verbose_name="id")
    name = models.CharField(max_length=255)


class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.URLField()
    url_to_image = models.URLField(name="urlToImage")
    published_date = models.DateTimeField(name="publishedAt")
    content = models.CharField(max_length=255)
    category = models.CharField(max_length=255)


class SavedArticle(models.Model):
    articles = models.ManyToManyField(Article)
    user_id = models.UUIDField()
