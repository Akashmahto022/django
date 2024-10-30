from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstapp, name="firstapp"),
    path('<int:user_id>',views.user_details, name="user-details" )
    
]
