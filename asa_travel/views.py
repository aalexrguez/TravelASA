from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Destination,Accommodation,ActivityAndTour\
                    ,FoodAndRestaurant,Attraction
# Create your views here.

def index(request):
    query = request.GET.get('q')
    if query:
        destination = Destination.objects.filter(name__contains=query)
    else:
        destination = Destination.objects.all()
    context = {
        'destinations':destination
    }
    return render(request,'asa_travel/index.html',context)

def destination_detail(request, destination_id):
    obj_destination = get_object_or_404(Destination, pk=destination_id)
    attraction = Attraction.objects.filter(attraction_destination=destination_id)
    accommodation = Accommodation.objects.filter(accommodation_destination=destination_id)
    activity = ActivityAndTour.objects.filter(at_destination=destination_id)
    fr = FoodAndRestaurant.objects.filter(fd_destination=destination_id)

    context = {
        'destination': obj_destination,
        'attractions': attraction,
        'accommodations': accommodation,
        'activities': activity,
        'restaurants': fr,
    }
    return render(request, 'asa_travel/destination_detail.html', context)

def registration(request):
    return render(request,'registration/register.html')