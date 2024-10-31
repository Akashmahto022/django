from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404

# Create your views here.


def firstapp(request):
    users = User.objects.all()
    return render(request, 'firstapp/first.html', {'users': users})

def user_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,'firstapp/user_details.html', {"user":user})

def user_store_view(request):
    return render(request, 'firstapp/app_store.html')


