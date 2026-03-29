from django.forms import ModelForm
from .models import Category, Article, Tag, ArticleTag, ArticleTranslation

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","category","author","status"]

class Tag(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

class ArticleTag(ModelForm):
    class Meta:
        model = ArticleTag
        fields = "__all__"

class ArticleTranslationForm(ModelForm):
    class Meta:
        model = ArticleTranslation
        fields = "__all__"
