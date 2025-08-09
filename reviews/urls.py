from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(),  name = "reviews-index"),
    path("submitted/", views.review_submitted, name="review-submitted")
]
