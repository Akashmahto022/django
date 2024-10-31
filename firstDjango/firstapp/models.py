from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    

# one to many
class UserReviw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    getUser = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.getUser.username} review for {self.user.name}'
        
# many to many relation

class Store(models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    userType = models.ManyToManyField(User, related_name='store')
    
    
    def __str__(self):
        return self.name
    
# one to one relation

class UserCertificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.user.name}'
    