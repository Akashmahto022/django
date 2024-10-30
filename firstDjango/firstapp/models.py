from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    USER_TYPE = [
        ('normal', "normaluser"),
        ('admin', "useradmin")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=120, blank=False, null=False, default='')
    description = models.TextField(max_length=500, blank=True,null=True)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=8, choices=USER_TYPE)

    
    
    def __str__(self):
        return self.name
    