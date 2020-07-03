from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
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


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Destination(models.Model):
    title = models.CharField(max_length=200, unique=True)
    tagline = models.CharField(max_length=200)
    slug = models.SlugField()
    img = models.ImageField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    DURA = (('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week'))
    duration = models.CharField(max_length=50, choices=DURA)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.CharField(max_length=200, unique=True)
    tagline = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField()
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    DURA = (('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week'))
    duration = models.CharField(max_length=50, choices=DURA)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("web:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("web:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("web:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

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