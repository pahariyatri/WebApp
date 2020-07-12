from django.contrib import admin
from .models import Destination, Cart, UserProfile, Price
from accounts.models import UserProfileInfo

admin.site.register(Destination)
admin.site.register(Cart)
admin.site.register(Price)
admin.site.register(UserProfile)

# Register your models here.
"""
admin.site.register(Thought)

class DestinationImageAdmin(admin.StackedInline):
    model = DestinationImage

class DestinationDayAdmin(admin.StackedInline):
    model = DestinationDay

class DestinationIncludeAdmin(admin.StackedInline):
    model = DestinationInclude
  
class DestinationExcludeAdmin(admin.StackedInline):
  model = DestinationExclude

admin.site.register(Booking)

admin.site.register(DestinationBooking)

@admin.register(Destination)
class DestinationsAdmin(admin.ModelAdmin)
    inlines = (DestinationImageAdmin, DestinationDayAdmin, DestinationIncludeAdmin, DestinationExcludeAdmin)  
    list_display = ("title", "duration",  "location")

    class Meta:
        model = Destination

"""