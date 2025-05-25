from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path("articles/", views.ArticleView.as_view()),
]
