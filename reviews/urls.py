from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(),  name = "reviews-index"),
    path("submitted/", views.SubittedView.as_view(), name="review-submitted"),
    path("reviews/", views.AllReviewsView.as_view(), name="all-reviews"),
    path("reviews/<int:id>", views.ReviewDetailView.as_view(), name="review-detail")
]
