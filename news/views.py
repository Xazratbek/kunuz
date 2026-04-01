from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category, ArticleTag, ArticleTranslation, Tag
from .forms import CategoryForm, ArticleForm, ArticleTranslationForm, TagForm, ArticleTagForm, EmailForm
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q
from django.conf import settings

class EmailSendView(View):
    def get(self, request):
        form = EmailForm()
        return render(request, "email/send.html",context={"form": form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            user_email = form.cleaned_data["user_email"]
            message = form.cleaned_data["message"]

            email_body = f"""
            Yangi xabar qabul qilindi:

            Yuboruvchi Email: {user_email}
            Mavzu: {subject}

            Xabar Matni:
            {message}
            """

            send_mail(
                subject=f"Yangi xabar: {subject}",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['xazratbek123@gmail.com'],
                fail_silently=False,
            )
            messages.success(request,"Email muvaffaqiyatli yuborildi ✅")
            return redirect("article-list")

        return render(request, "email/send.html", context={"form": form})

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(status="published").order_by("-created_at")
        page_num = request.GET.get("page")
        paginator = Paginator(articles, 10)
        page_obj = paginator.get_page(page_num)

        latest_articles = Article.objects.filter(status="published").order_by("-created_at")[:6]

        categories = Category.objects.filter(parent__isnull=True)[:5]
        category_articles = {}
        for category in categories:
            category_articles[category] = category.articles.filter(status="published").order_by("-created_at")[:4]

        return render(request, "articles/list.html", context={
            "articles": page_obj,
            "latest_articles": latest_articles,
            "category_articles": category_articles,
        })

class ArticleCreateView(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, "articles/create.html",context={"form": form})

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("article-list")

class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug,status="published")
        return render(request, "articles/detail.html",context={"article": article})

class ArticleDeleteView(View):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.delete()
        return redirect("article-list")

class ArticleUpdateView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        form = ArticleForm(instance=article)
        return render(request,"articles/update.html",context={"form": form, "article": article})

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article-list")

        return render(request,"articles/update.html",context={"form": form,"article": article})

class CategoryNews(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        news = category.articles.all()
        return render(request,"articles/category-news.html",context={"category": category, "news": news})


class ArticleSearchView(View):
    def get(self, request):
        q = request.GET.get("q","")
        articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

        return render(request, "articles/search.html",context={"articles": articles})

class ArticleTranslationView(View):
    def get(self, request, lang):
        articles = ArticleTranslation.objects.filter(language=lang)

        lang_name = "Ruscha" if lang == "ru" else "Inglizcha" if lang == "en" else "O'zbekcha"

        return render(request,"articles/article_translations_list.html",context={
            "articles": articles,
            "language": lang,
            "language_name": lang_name
        })

class ArticleTranslationDetail(View):
    def get(self,request, lang, slug):
        article = get_object_or_404(ArticleTranslation, language=lang, slug=slug)
        return render(request,"articles/article_translation_detail.html",context={"article": article})