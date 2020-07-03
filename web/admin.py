from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',

                    'refund_requested',
                    'refund_granted',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',


                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
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