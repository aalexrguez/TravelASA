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
