from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path("", views.TourView.as_view()),
    path("<uuid:pk>/", views.TourDetailView.as_view()),
    path("faq/", views.FAQView.as_view()),
]
