from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
class CreateProfileView(CreateView):
    template_name = "profiles/index.html"
    model = UserProfile
    #form_class = UserProfileForm
    fields = "__all__"
    
    success_url = "/profiles"
