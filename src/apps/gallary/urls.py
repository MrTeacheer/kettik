from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path('place/',views.PlaceView.as_view()),
]