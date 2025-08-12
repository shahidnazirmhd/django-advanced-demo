from django.urls import path


from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="profile-index"),
    path("list/", views.ListProfileView.as_view(), name="profile-list"),
]