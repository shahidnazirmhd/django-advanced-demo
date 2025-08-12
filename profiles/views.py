from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
class CreateProfileView(View):
    def get(self, request):
        form = UserProfileForm()
        return render(request, "profiles/index.html", { "form": form})

    def post(self, request):
        submitted_form = UserProfileForm(request.POST, request.FILES)
        print("TESTETSTEST")
        if submitted_form.is_valid():
            # profile = UserProfile(profile=request.FILES["profile"])
            # profile.save()
            submitted_form.save()
            return HttpResponseRedirect("/profiles/")
        return HttpResponseRedirect("/profiles/", {"form": submitted_form})
