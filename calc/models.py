from django.db import models


# Create your models here.

"""
class Destination :
    id: int
    name: str
    img: str
    price: int
 """
class Home_background(models.Model):
    text_large = models.CharField(max_length=15)
    text_small = models.CharField(max_length=25)
    background_image = models.ImageField(upload_to='pics')


class Upcoming_destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()


class Popular_destinations(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()

class Special_offers(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')

class Thought(models.Model):
    text = models.CharField(max_length=1000)

class Event(models.Model):
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    destination = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    day = models.IntegerField()
    night = models.IntegerField()
    detail = models.CharField(max_length=1000)


    def __set__(self):
        return self.destination

class Trip(models.Model):
    destinations = models.CharField(max_length=50)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    emergencycontact = models.IntegerField()
    country = models.CharField(max_length=20)
    date = models.DateField()
    numberofadult = models.IntegerField()
    question = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return  self.destinations

class Description(models.Model):
    title = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    img3 = models.ImageField(upload_to='pics')


class Overview(models.Model):
    over_view = models.CharField(max_length=500)
    about_location = models.CharField(max_length=500)
    about_destination = models.CharField(max_length=500)
    why_choose_us = models.CharField(max_length=500)
    price = models.IntegerField()
    duration = models.IntegerField()
    grade = models.CharField(max_length=20)
    best_time = models.CharField(max_length=100)

