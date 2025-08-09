from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from . import forms

# Create your views here.
class ReviewView(View):
    def get(self, request):
        review_form = forms.ReviewForm()
        return render(request, "reviews/index.html", {"form": review_form})



    def post(self, request):
        review_form = forms.ReviewForm(request.POST)   # Use instance parameter for update in DB
        if review_form.is_valid():
            print(review_form.cleaned_data)
            review_form.save()
            return HttpResponseRedirect("/submitted")
        
        return render(request, "reviews/index.html", {"form": review_form})



def review_submitted(request):
    return render(request, "reviews/submitted.html",)