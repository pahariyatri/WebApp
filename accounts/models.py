from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    thought = models.CharField(max_length=1000)
    pic = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
         return self.user.username


