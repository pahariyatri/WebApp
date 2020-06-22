from django.shortcuts import render, redirect, get_object_or_404
from .models import Thought
from math import ceil
from .models import Destination, DestinationImage, DestinationDay, DestinationInclude, DestinationExclude
from django.http import *
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime, timedelta
startdate = datetime.today()
enddate = startdate + timedelta(days=154)

def index(request):

    ev = Destination.objects.filter(date__range=[startdate, enddate])[:3]
    eve = Destination.objects.all()[:12:-1]
    thought = Thought.objects.all()
    allProds = []
    catprods = Destination.objects.values('region', 'id')
    cats = {item['region'] for item in catprods}
    for cat in cats:
        prod = Destination.objects.filter(region=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    adventure = Destination.objects.filter(categories='ADVENTURE').count()
    solo = Destination.objects.filter(categories='SOLO').count()
    nature = Destination.objects.filter(categories='NATURE').count()
    group = Destination.objects.filter(categories='GROUP').count()
    family = Destination.objects.filter(categories='FAMILY').count()
    religous = Destination.objects.filter(categories="RELIGOUS").count()
    romantic = Destination.objects.filter(categories="COUPLE").count()
    water_act = Destination.objects.filter(categories="WATER_ACTIVITIES").count()

    d = {
        "even": eve,
        "ev": ev,
        "thoug": thought,
        "allProds":allProds,
        "adventure":adventure,
        "nature": nature,
        "solo":solo,
        "group":group,
        "romantic":romantic,
        "family":family,
        "religous":religous,
        "water_act":water_act,
    }

    return render(request, 'index.html', d)

def offers(request):
    page_title='All Destinations'
    eve = Destination.objects.all()
    c = Destination.objects.all().count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

#class HomePageView(TemplateView):
    template_name = 'index.html'

def details(request, pk_test):
    ev = Destination.objects.get(id=pk_test)
    destination = get_object_or_404(Destination, id=pk_test)
    destinations = get_object_or_404(Destination, id=pk_test)
    dest = get_object_or_404(Destination, id=pk_test)
    photos = DestinationImage.objects.filter(destination=destination)
    a = DestinationDay.objects.filter(destination=destination)[0:10:-1]
    b = DestinationInclude.objects.filter(destination=destination)
    c = DestinationExclude.objects.filter(destination=destination)

    eve = {
        "destination":destination,
        "destinations": destinations,
        "dest":dest,
        "photos":photos,
        "ev":ev,
        "a":a,
        "b":b,
        "c":c,
    }

    return render(request, 'dest_details.html' ,eve)


class SearchResultsView(ListView):
    model = Destination
    template_name = 'destination.html'
    page_title='SearchResults'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Destination.objects.filter(
            Q(name__exact=query) | Q(categories__exact=query)
        )
        return object_list


def adventure(request):
#    eve = Destinations.objects.all()
    page_title= 'Adventure'
    eve = Destination.objects.filter(categories='ADVENTURE')
    c = Destination.objects.filter(categories='ADVENTURE').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)



def solo(request):
#    eve = Destinations.objects.all()
    page_title= 'Solo'
    eve = Destination.objects.filter(categories='SOLO')
    c = Destination.objects.filter(categories='SOLO').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def group(request):
#    eve = Destinations.objects.all()
    page_title= 'Group'
    eve = Destination.objects.filter(categories='GROUP')
    c = Destination.objects.filter(categories='GROUP').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)


def religous(request):
#    eve = Destinations.objects.all()
    page_title= 'Religous'
    eve = Destination.objects.filter(categories='RELIGOUS')
    c = Destination.objects.filter(categories='RELIGOUS').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def wateractivities(request):
#    eve = Destinations.objects.all()
    page_title= 'Water Activitities'
    eve = Destination.objects.filter(categories='WATER_ACTIVITIES')
    c = Destination.objects.filter(categories='WATER_ACTIVITIES').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def nature(request):
#    eve = Destinations.objects.all()
    page_title= 'Nature'
    eve = Destination.objects.filter(categories='NATURE')
    c = Destination.objects.filter(categories='NATURE').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def family(request):
#    eve = Destinations.objects.all()
    page_title= 'Family'
    eve = Destination.objects.filter(categories='FAMILY')
    c = Destination.objects.filter(categories='FAMILY').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def romantic(request):
#    eve = Destinations.objects.all()
    page_title= 'Romantic'
    eve = Destination.objects.filter(categories='COUPLE')
    c = Destination.objects.filter(categories='COUPLE').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)