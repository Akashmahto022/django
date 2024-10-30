from django.shortcuts import render
from .models import User

# Create your views here.


def firstapp(request):
    users = User.objects.all()
    return render(request, 'firstapp/first.html', {'users': users})