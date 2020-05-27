from django.shortcuts import render, redirect
from .models import Special_offers, Home_background, Thought
from .models import Destinations
from django.http import *
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime, timedelta
#startdate = datetime.today()
#enddate = startdate + timedelta(days=9)

def index(request):

#    eve = Destinations.objects.filter(date__range=[startdate, enddate])
    eve = Destinations.objects.all()[:3]
    soffers = Special_offers.objects.all()
    home = Home_background.objects.all()
    thought = Thought.objects.all()
    adventure = Destinations.objects.filter(categories='ADVENTURE').count()
    solo = Destinations.objects.filter(categories='SOLO').count()
    nature = Destinations.objects.filter(categories='NATURE').count()
    group = Destinations.objects.filter(categories='GROUP').count()
    family = Destinations.objects.filter(categories='FAMILY').count()
    religous = Destinations.objects.filter(categories="RELIGOUS").count()
    romantic = Destinations.objects.filter(categories="ROMANTIC").count()
    water_act = Destinations.objects.filter(categories="WATER_ACTIVITIES").count()

    d = {

        "even": eve,
        "home_back": home,
        "special_offers": soffers,
        "thoug": thought,
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
    eve = Destinations.objects.all()
    c = Destinations.objects.all().count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

#class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Destinations
    template_name = 'destination.html'
    page_title='SearchResults'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Destinations.objects.filter(
            Q(name__exact=query) | Q(categories__exact=query)
        )

        return object_list

def adventure(request):
#    eve = Destinations.objects.all()
    page_title= 'Adventure'
    eve = Destinations.objects.filter(categories='ADVENTURE')
    c = Destinations.objects.filter(categories='ADVENTURE').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)



def solo(request):
#    eve = Destinations.objects.all()
    page_title= 'Solo'
    eve = Destinations.objects.filter(categories='SOLO')
    c = Destinations.objects.filter(categories='SOLO').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def group(request):
#    eve = Destinations.objects.all()
    page_title= 'Group'
    eve = Destinations.objects.filter(categories='GROUP')
    c = Destinations.objects.filter(categories='GROUP').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)


def religous(request):
#    eve = Destinations.objects.all()
    page_title= 'Religous'
    eve = Destinations.objects.filter(categories='RELIGOUS')
    c = Destinations.objects.filter(categories='RELIGOUS').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def wateractivities(request):
#    eve = Destinations.objects.all()
    page_title= 'Water Activitities'
    eve = Destinations.objects.filter(categories='WATER_ACTIVITIES')
    c = Destinations.objects.filter(categories='WATER_ACTIVITIES').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def nature(request):
#    eve = Destinations.objects.all()
    page_title= 'Nature'
    eve = Destinations.objects.filter(categories='NATURE')
    c = Destinations.objects.filter(categories='NATURE').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def family(request):
#    eve = Destinations.objects.all()
    page_title= 'Family'
    eve = Destinations.objects.filter(categories='FAMILY')
    c = Destinations.objects.filter(categories='FAMILY').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)

def romantic(request):
#    eve = Destinations.objects.all()
    page_title= 'Romantic'
    eve = Destinations.objects.filter(categories='ROMANTIC')
    c = Destinations.objects.filter(categories='ROMANTIC').count()

    ev = {
        "even": eve,
        "c":c,
        "page_title": page_title,
    }
    return render(request, 'destination.html',ev, c)