from django.shortcuts import render

# Create your views here.
def reviews_index(request):
    return render(request, "reviews/index.html",)