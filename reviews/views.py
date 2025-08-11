from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .models import Review

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



# def review_submitted(request):
#     return render(request, "reviews/submitted.html",)
class SubittedView(TemplateView):
    template_name = "reviews/submitted.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emoji"] = "🫶"
        return context
    

class AllReviewsView(TemplateView):
    template_name = "reviews/all-reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews 
        return context
    

class ReviewDetailView(TemplateView):
    template_name = "reviews/review-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(pk=review_id)
        context["review"] = review
        return context
    
    
    