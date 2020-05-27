from django.contrib import admin
from .models import *

# Register your models here.

class DestinationsAdmin(admin.ModelAdmin):
    list_display = ("name", "categories","duration","price","img","region")
admin.site.register(Destinations, DestinationsAdmin)
admin.site.register(Special_offers)
admin.site.register(Home_background)
admin.site.register(Thought)
