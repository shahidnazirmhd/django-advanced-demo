from django.urls import path

from . import views
urlpatterns = [
    path("", views.reviews_index,  name = "reviews-index")
]
