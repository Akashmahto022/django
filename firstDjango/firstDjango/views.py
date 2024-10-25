from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("hello world, Akash kumar")
    return render(request, 'website/home.html')

def name(request):
    return render(request, "website/name.html")

def contact(request):
    return render(request, "website/contact.html")

def about(request):
    return render(request, "website/about.html")


