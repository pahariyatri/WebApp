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
    detail = models.CharField(max_length=1000, blank=True)

    date = models.DateField()


    def __set__(self):
        return self.name

    """
    class Upcoming_destination :
        id: int
        name: str
        img: str
        price: int
        detail: str
     """


class Popular_destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    detail = models.CharField(max_length=1000, blank=True)
    CHOICES = (('a', 'Advan'), ('w', 'WildLife'), ('f', 'Widthfrandes'), ('s', 'solo'))
    type = models.CharField(max_length=30, choices=CHOICES)
    date = models.DateField()

class Special_offers(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')

class Thought(models.Model):
    text = models.CharField(max_length=1000)


