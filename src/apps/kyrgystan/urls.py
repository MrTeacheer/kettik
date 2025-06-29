from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path("articles/", views.ArticleView.as_view()),
    path("regions", views.RegionView.as_view()),
]
