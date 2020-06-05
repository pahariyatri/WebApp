from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(Thought)

class DestinationImageAdmin(admin.StackedInline):
    model = DestinationImage

class DestinationDayAdmin(admin.StackedInline):
    model = DestinationDay

class DestinationIncludeAdmin(admin.StackedInline):
    model = DestinationInclude

class DestinationExcludeAdmin(admin.StackedInline):
    model = DestinationExclude

@admin.register(Destination)
class DestinationsAdmin(admin.ModelAdmin):
    inlines = (DestinationImageAdmin, DestinationDayAdmin, DestinationIncludeAdmin, DestinationExcludeAdmin)
    list_display = ("name", "categories", "duration", "price", "img", "region")

    class Meta:
        model = Destination

