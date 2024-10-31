from django.shortcuts import render
from .models import User, Store
from django.shortcuts import get_object_or_404
from .forms import UserTypeForm

# Create your views here.


def firstapp(request):
    users = User.objects.all()
    return render(request, 'firstapp/first.html', {'users': users})

def user_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,'firstapp/user_details.html', {"user":user})

def user_store_view(request):
    stores = None
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            stores = Store.objects.filter(userType=user_type)
            
    
    else:
        form = UserTypeForm()
    return render(request, 'firstapp/app_store.html', {'stores': stores, 'form': form})


