import googlemaps
from django.conf import settings
from django.db import models
from django.db.models import Manager
from django.db.models import Sum
from django.shortcuts import reverse
from multiselectfield import MultiSelectField
from datetime import datetime
from django_countries.fields import CountryField

# Create your models here.

"""
class Destination :
    id: int
    name: str
    img: str
    price: int
 """

"""
class Upcoming_destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    detail = models.CharField(max_length=1000, blank=True)
    CHOICES = (('a', 'Adventure'), ('w', 'WildLife'), ('s', 'solo'))
    type = models.CharField(max_length=30, choices=CHOICES)
    date = models.DateField()


    def __set__(self):
        return self.name




class Popular_destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    detail = models.CharField(max_length=1000, blank=True)
    CHOICES = (('a', 'Advan'), ('w', 'WildLife'), ('f', 'Widthfrandes'), ('s', 'solo'))
    type = models.CharField(max_length=30, choices=CHOICES)
    date = models.DateField()
    """

STATUS = (
    (0, "Hide"),
    (1, "Publish")
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    DURA = (('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week'))
    duration = models.CharField(max_length=50, choices=DURA)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Price(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    charge = models.IntegerField(default=1000)
    tent = models.IntegerField()
    guide = models.IntegerField()
    meal = models.IntegerField()

    def __str__(self):
        return f"{self.get_absolute_url} of {self.destination.title}"


    @property
    def gross(self):
        return self.tent + self.guide + self.meal

    @property
    def get_absolute_url(self):
        return self.gross + self.charge


class PriceManager(models.Manager):
    def create_price(self, destination):
        price = self.create(destination=destination)
        # do something with the book
        return price


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    objects = PriceManager()

    def __str__(self):
        return f"{self.quantity} of {self.destination.title}"

    def total_price(self):
        return self.quantity * self.destination.price


"""
class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    img = models.ImageField(upload_to='pic', blank=True)


class DestinationDay(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    day_heading = models.CharField(max_length=100)
    day = models.CharField(max_length=1000, blank=True)

class DestinationInclude(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    accommodation = models.CharField(max_length=200, blank=True)
    guide = models.CharField(max_length=200, blank=True)
    meals = models.CharField(max_length=200, blank=True)
    transport = models.CharField(max_length=200, blank=True)
    additional = models.CharField(max_length=200, blank=True)

class DestinationExclude(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    list = models.CharField(max_length=300, blank=True)
"""
