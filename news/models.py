from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
