from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
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

def destination_detail(request,destination_id):
    obj_destination = Destination.objects.get(pk=destination_id)
    context = {
        'destination':obj_destination
    }
    return render(request,'asa_travel/destination_detail.html',context)
