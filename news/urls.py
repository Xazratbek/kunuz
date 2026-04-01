from django.urls import path, re_path
from .views import EmailSendView, ArticleListView,ArticleDetailView, CategoryNews, ArticleSearchView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ArticleTranslationView, ArticleTranslationDetail

urlpatterns = [
    path("",ArticleListView.as_view(),name="article-list"),
    path("create/",ArticleCreateView.as_view(),name="article-create"),
    path("update/<str:slug>/",ArticleUpdateView.as_view(),name="article-update"),
    path("delete/<str:slug>/",ArticleDeleteView.as_view(),name="article-delete"),
    path("search/", ArticleSearchView.as_view(), name="search"),
    path("email/send/",EmailSendView.as_view(),name="send-email"),
    path("category/<str:slug>/",CategoryNews.as_view(),name="category-news"),

    re_path(r'^(?P<lang>ru|en|uz)/$', ArticleTranslationView.as_view(), name="article-translaations-ru"),
    re_path(r'^(?P<lang>ru|en|uz)/category/(?P<slug>[a-z0-9\-]+)/$', CategoryNews.as_view(), name="category-news-lang"),
    re_path(r'^(?P<lang>ru|en|uz)/(?P<slug>[a-z0-9\-]+)/$', ArticleTranslationDetail.as_view(), name="article-translation-detail"),

    path("<str:slug>/",ArticleDetailView.as_view(),name="article-detail"),
]
