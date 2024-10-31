from django import forms
from .models import User

class UserTypeForm(forms.Form):
    user_type = forms.ModelChoiceField(queryset=User.objects.all(), label="select user type")
    # user_type = forms.CharField()
    
    