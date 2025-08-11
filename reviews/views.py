from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import Review

from .forms import ReviewForm

# Create your views here.
class ReviewView(FormView):
    template_name = "reviews/index.html"
    form_class = ReviewForm
    
    success_url = "/submitted"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


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
    
    
    