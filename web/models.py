from django.db import models

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


class Thought(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pics')


class Destination(models.Model):
    REG = (('Himachal Pradesh', 'Himachal Pradesh'), ('Uttarakhand', 'Uttarakhand'),
           ('Jammu and Kashmir', 'Jammu and Kashmir'), ('leh ladakh', 'leh ladakh'),
           ('Meghalaya', 'Meghalaya'), ('Sikkim', 'Sikkim'), ('Goa', 'Goa'),
           ('Rajasthan', 'Rajasthan'), ('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'))
    DURA = (('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week'))
    CATE = (('ADVENTURE', 'ADVENTURE'), ('SOLO', 'SOLO'),
            ('GROUP', 'GROUP'), ('RELIGOUS', 'RELIGOUS'),
            ('WATER_ACTIVITIES', 'WATER_ACTIVITIES'), ('NATURE', 'NATURE'),
            ('FAMILY', 'FAMILY'), ('COUPLE', 'COUPLE'))
    name = models.CharField(max_length=100)
    small_description = models.CharField(max_length=200)
    img = models.ImageField()
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    region = models.CharField(max_length=30, choices=REG)
    full_description = models.CharField(max_length=150)
    continue_description = models.CharField(max_length=5000, blank=True)
    mythological = models.CharField(max_length=5000, blank=True)
    destination_covered = models.CharField(max_length=200, blank=True)
    categories = models.CharField(max_length=30, choices=CATE)
    duration = models.CharField(max_length=50, choices=DURA)
    date = models.DateField()


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    img = models.ImageField(upload_to='pic')


class DestinationDay(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, )
    day_heading = models.CharField(max_length=100)
    day = models.CharField(max_length=1000)


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

