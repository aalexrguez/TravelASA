from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Destination,Accommodation,ActivityAndTour\
                    ,FoodAndRestaurant,Attraction,Client,Review
from .forms import ClientForm,ReviewForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {'error': 'El nombre de usuario ya existe.'})

        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        
        login(request, user)
        return redirect('/')

    return render(request, 'registration/register.html')

def review(request):
    if request.method == 'POST':
        frmReview = ReviewForm(request.POST)
        if frmReview.is_valid():
            dataReview = frmReview.cleaned_data
            destination = dataReview['destination']
            comment = dataReview['comment']
            rating = dataReview['rating']

            Review.objects.create(
                review_user = request.user,
                review_destination = destination,
                review_comment = comment,
                review_rating = rating
            )

            return redirect('/')
            
    else:
        frmReview = ReviewForm()
    context = {
        'frmReview':frmReview,
    }
    return render(request,'asa_travel/review.html',context)

