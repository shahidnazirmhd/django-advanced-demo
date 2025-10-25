from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .models import Review

from .forms import ReviewForm

# Create your views here.
class ReviewView(CreateView):
    template_name = "reviews/index.html"
    model = Review
    form_class = ReviewForm
    
    success_url = "/submitted"
    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id) 
        return context
    


class AddFavoriteView(View):
    def post(self, requests):
        review_id = requests.POST["review_id"]
        requests.session["favorite_review"] = review_id
        #return HttpResponseRedirect("/reviews/" + review_id)
        return redirect("review-detail", pk=review_id)
    
    