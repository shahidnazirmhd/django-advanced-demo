from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def reviews_index(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponseRedirect("/submitted")
    return render(request, "reviews/index.html",)


def review_submitted(request):
    return render(request, "reviews/submitted.html",)