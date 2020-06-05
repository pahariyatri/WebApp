import django_filters
from packages .models import Destinations

class DestinationFilter(django_filters.FilterSet):
    class Meta:
        model = Destinations
        fields = {

            'categories': ['icontains', 'istartswith', 'iendswith'],
        }