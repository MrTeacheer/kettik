from django.urls import path
from . import views

urlpatterns = [
    path("banner/", views.BannerView.as_view()),
    path("application/", views.ApplicationView.as_view()),
    path('contacts/',views.ContactsView.as_view()),
    path('google/reviews/',views.GoogleReviewsView.as_view()),
]
