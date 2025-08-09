from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
from .models import Review
# Create your views here.
def reviews_index(request):
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)   # Use instance parameter for update in DB
        if review_form.is_valid():
            print(review_form.cleaned_data)
            # Review.objects.create(
            #     full_name=review_form.cleaned_data["full_name"],
            #     email=review_form.cleaned_data["email"],
            #     rating=review_form.cleaned_data["rating"],
            #     message=review_form.cleaned_data["message"]
            # )
            review_form.save()
            return HttpResponseRedirect("/submitted")
    else:
        review_form = forms.ReviewForm()
    return render(request, "reviews/index.html", {"form": review_form})


def review_submitted(request):
    return render(request, "reviews/submitted.html",)