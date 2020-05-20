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

    
    class Upcoming_destination :
        id: int
        name: str
        img: str
        price: int
        detail: str
     


class Popular_destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    detail = models.CharField(max_length=1000, blank=True)
    CHOICES = (('a', 'Advan'), ('w', 'WildLife'), ('f', 'Widthfrandes'), ('s', 'solo'))
    type = models.CharField(max_length=30, choices=CHOICES)
    date = models.DateField()
    """

class Special_offers(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')

class Thought(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pics')

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    detail = models.CharField(max_length=1000, blank=True)
    region = models.CharField(max_length=100)
    DURA = (('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week'))
    CATE = (('SOLO', 'SOLO'), ('GROUP', 'GROUP'), ('FAMILY', 'FAMILY'), ('ROMANTIC', 'ROMANTIC'))
    ACTI = (('ADVENTURE', 'ADVENTURE'), ('WILDLIFE', 'WILDLIFE'),('RELIGOUS', 'RELIGOUS'), ('WATER_ACTIVITIES', 'WATER_ACTIVITIES'))
    categories = models.CharField(max_length=30, choices=CATE)
    activities = models.CharField(max_length=30, choices=ACTI)
    duration = models.CharField(max_length = 50, choices=DURA)
    date = models.DateField()






