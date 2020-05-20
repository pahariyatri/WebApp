from django.shortcuts import render, redirect
from .models import Special_offers, Home_background, Thought
from .models import Destinations
from django.http import *
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime, timedelta
startdate = datetime.today()
enddate = startdate + timedelta(days=9)

def index(request):
    eve = Destinations.objects.filter(date__range=[startdate, enddate])
    soffers = Special_offers.objects.all()
    home = Home_background.objects.all()
    thought = Thought.objects.all()
    adventure = Destinations.objects.filter(activities='ADVENTURE').count()
    wildlife = Destinations.objects.filter(activities='WILDLIFE').count()
    religous = Destinations.objects.filter(activities="RELIGOUS").count()
    water_act = Destinations.objects.filter(activities="WATER_ACTIVITIES").count()

    d = {
        "even": eve,
        "home_back": home,
        "special_offers": soffers,
        "thoug": thought,
        "adventure":adventure,
        "wildlife":wildlife,
        "religous":religous,
        "water_act":water_act,
    }
    print(adventure)
    print(wildlife)
    print(religous)
    print(water_act)
    return render(request, 'index.html', d)

def offers(request):
    eve = Destinations.objects.all()
    c = Destinations.objects.all().count()

    ev = {
        "even": eve,
        "c":c
    }
    print('********')
    print (c)
    print(type(c))
    return render(request, 'destination.html',ev, c)

#class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Destinations
    template_name = 'destination.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Destinations.objects.filter(
            Q(name__exact=query) | Q(categories__exact=query)
        )
        return object_list
