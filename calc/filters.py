import django_filters
from django_filters import CharFilter

from .models import *

class DestinationFilter(django_filters.FilterSet):


    class Meta:
        model = Popular_destinations
        fields = {
            'name': ['icontains', 'istartswith', 'iendswith',],
            'type': ['icontains', 'istartswith', 'iendswith'],
        }