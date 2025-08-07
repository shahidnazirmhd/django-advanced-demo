from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
# Create your views here.
def reviews_index(request):
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            print(review_form.cleaned_data)
            return HttpResponseRedirect("/submitted")
    review_form = forms.ReviewForm()
    return render(request, "reviews/index.html", {"form": review_form})


def review_submitted(request):
    return render(request, "reviews/submitted.html",)