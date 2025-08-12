from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
class CreateProfileView(CreateView):
    template_name = "profiles/index.html"
    model = UserProfile
    #form_class = UserProfileForm
    fields = "__all__"
    
    success_url = "/profiles"


class ListProfileView(ListView):
    template_name = "profiles/list.html"
    model = UserProfile
    context_object_name = "user_profiles"
