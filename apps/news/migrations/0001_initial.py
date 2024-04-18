# Generated by Django 5.0.4 on 2024-04-09 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("url", models.URLField()),
                ("urlToImage", models.URLField()),
                ("publishedAt", models.DateTimeField()),
                ("content", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source_id", models.CharField(max_length=255, verbose_name="id")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SavedArticle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.UUIDField()),
                ("article", models.ManyToManyField(to="news.article")),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="news.source"
            ),
        ),
    ]