from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
from django.urls import reverse

class ArticleStatusChoice(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"

class LanguageChoice(models.TextChoices):
    RU = "ru", "Ruscha"
    EN = "en", "Inglizcha"

class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name="Kategoriya nomi")
    parent = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250,verbose_name="Sarlavha")
    slug = models.SlugField(unique=True)
    content = CKEditor5Field(verbose_name="Maqola matni")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="articles")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    status = models.CharField(max_length=20,choices=ArticleStatusChoice.choices, default=ArticleStatusChoice.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=150,verbose_name="Tag nomi",help_text="Tag nomini kiriting")

    def __str__(self):
        return self.name

class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)

class ArticleTranslation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,verbose_name="Maqola")
    language = models.CharField(max_length=10,choices=LanguageChoice.choices)
    title = models.CharField(max_length=150)
    content = CKEditor5Field(verbose_name="Maqola to'liq matni")