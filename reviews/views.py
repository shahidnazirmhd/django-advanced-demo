from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

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



class SubittedView(TemplateView):
    template_name = "reviews/submitted.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emoji"] = "🫶"
        return context
    

class AllReviewsView(ListView):
    template_name = "reviews/all-reviews.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     queryset = base_query.filter(rating__gte=4)
    #     return queryset
    
    

class ReviewDetailView(DetailView):
    template_name = "reviews/review-detail.html"
    model = Review
    
    
    