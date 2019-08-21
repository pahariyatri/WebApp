from django.shortcuts import render

# Create your views here.

from  .models import  Destination
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 7000
    dest1.img = 'top_1.jpg'

    dest2 = Destination()
    dest2.name = 'hyderabad'
    dest2.price = 8000
    dest2.img = 'top_2.jpg'

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.price = 7050
    dest3.img = 'top_3.jpg'

    dest4 = Destination()
    dest4.name = 'Delhi'
    dest4.price = 10000
    dest4.img = 'top_4.jpg'

    dests = [dest1, dest2, dest3, dest4]

    return render(request, 'index.html', {'dests':dests})