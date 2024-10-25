from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("hello world, Akash kumar")
    return render(request, 'website/home.html')



def name(request):
    return HttpResponse("hello name, Akash kumar")

def contact(request):
    return HttpResponse("hello contact, Akash kumar")

def about(request):
    return HttpResponse("hello about, Akash kumar")



