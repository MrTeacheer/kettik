from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path("history/", views.HistoryView.as_view()),
    path("images/", views.ImagesView.as_view()),
    path("in/digits/", views.InDigitsView.as_view()),
    path('teams/',views.TeamView.as_view()),
]
