from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Popular_destinations, Upcoming_destination, Special_offers, Home_background, Description, Overview, Thought, Event, Trip

from .forms import Tripform

def index(request):
    pdests = Popular_destinations.objects.all()
    dests = Upcoming_destination.objects.all()
    soffers = Special_offers.objects.all()
    home = Home_background.objects.all()
    thought = Thought.objects.all()

    destination = {
        "home_back": home,
        "popular_dest": pdests,
        "top_dest": dests,
        "special_offers": soffers,
        "thoug": thought
    }
    return render(request, 'index.html', destination)



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def offers(request):
    eve = Event.objects.all()
    ev = {
        "even": eve
    }
    return render(request, 'offers.html',ev)

def news(request):
    return render(request, 'news.html')

