from django.forms import ModelForm
from .models import Category, Article, Tag, ArticleTag, ArticleTranslation
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","category","status"]
        widgets = {
            "content": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends")
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

class ArticleTagForm(ModelForm):
    class Meta:
        model = ArticleTag
        fields = "__all__"

class ArticleTranslationForm(ModelForm):
    class Meta:
        model = ArticleTranslation
        fields = "__all__"
        widgets = {
            "content": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends")
        }

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=150)
    user_email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.widgets.Textarea)