# Generated by Django 5.0.4 on 2024-04-10 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="savedarticle",
            old_name="article",
            new_name="articles",
        ),
    ]
