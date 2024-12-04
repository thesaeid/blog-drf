# Generated by Django 5.1.3 on 2024-12-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="blog_posts", to="post.tag"
            ),
        ),
    ]