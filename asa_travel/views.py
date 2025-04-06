from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):
    destination_all = Destination.objects.all()
    context = {
        'destinations':destination_all
    }
    return render(request,'asa_travel/index.html',context)