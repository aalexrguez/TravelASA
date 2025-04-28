from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Destination,Accommodation,ActivityAndTour\
                    ,FoodAndRestaurant,Attraction,Client,Review
from .forms import ClientForm,ReviewForm,AttractionForm,\
                   RestaurantForm,AccommodationForm,ActivityForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    query = request.GET.get('q')
    if query:
        destination = Destination.objects.filter(destination_name__contains=query)
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
    reviews = Review.objects.filter(review_destination=destination_id)

    context = {
        'destination': obj_destination,
        'attractions': attraction,
        'accommodations': accommodation,
        'activities': activity,
        'restaurants': fr,
        'reviews':reviews
    }
    return render(request, 'asa_travel/destination_detail.html', context)

"""LOGIN"""

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


"""Reseñas """

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

def my_reviews(request):
    user_reviews = Review.objects.filter(review_user=request.user)
    context = {
        'user_reviews':user_reviews
    }
    return render(request,'asa_travel/my_reviews.html',context)


def update_review(request,review_id):
    review = get_object_or_404(Review,id=review_id,review_user=request.user)
    if request.method == 'POST':
        frmReview = ReviewForm(request.POST)
        if frmReview.is_valid():
            dataReview = frmReview.cleaned_data
            review.review_destination = dataReview['destination']
            review.review_comment = dataReview['comment']
            review.review_rating = dataReview['rating']
            review.save()
            return redirect('/my_reviews/')
    else:
        frmReview = ReviewForm(initial={
        'destination': review.review_destination,
        'comment': review.review_comment,
        'rating': review.review_rating,
    })
    
    context = {
        'frmReview':frmReview,
        'review':review
    }
    return render(request,'asa_travel/update_review.html',context)

def delete_review(request,review_id):
    review = get_object_or_404(Review,id=review_id,review_user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('asa_travel/reviews.html/')
    
    context = {
        'review':review
    }
    
    return render(request,'asa_travel/my_reviews.html',context)

""" Categorias del destino """
def attraction(request,destination_id):
    attraction = Attraction.objects.get(id=destination_id)
    context = {
        'attractions':attraction
    }
    return render(request,'asa_travel/attraction.html',context)

def activities(request,destination_id):
    activities = ActivityAndTour.objects.get(id=destination_id)
    context = {
        'activities':activities
    }
    return render(request,'asa_travel/activities.html',context)

def restaurant(request,restaurant_id):
    restaurant = FoodAndRestaurant.objects.get(id=restaurant_id)
    context = {
        'restaurant':restaurant
    }
    return render(request,'asa_travel/restaurant.html',context)

def accommodation(request,accommodation_id):
    accommodation = Accommodation.objects.get(id=accommodation_id)
    context = {
        'accommodation':accommodation
    }
    return render(request,'asa_travel/accommodation.html',context)

"""VISTAS ADMIN EDICION"""
def edit_attraction(request, attraction_id):
    attraction = get_object_or_404(Attraction, id=attraction_id)

    if request.method == 'POST':
        frmAttraction = AttractionForm(request.POST, request.FILES, instance=attraction)
        if frmAttraction.is_valid():
            frmAttraction.save()
            return redirect('/') 
    else:
        frmAttraction = AttractionForm(instance=attraction)

    context = {
        'frmAttraction': frmAttraction
    }
    return render(request, 'asa_travel/edit_attraction.html',context)

def edit_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(FoodAndRestaurant,id=restaurant_id)

    if request.method == 'POST':
        frmRestaurant = RestaurantForm(request.POST,request.FILES,instance=restaurant)
        if frmRestaurant.is_valid():
            frmRestaurant.save()
            return redirect('/')
    else:
        frmRestaurant = RestaurantForm(instance=restaurant)
    
    context = {
        "frmRestaurant":frmRestaurant
    }

    return render(request,'asa_travel/edit_restaurant.html',context)

def edit_accommodation(request,accommodation_id):
    accommodation = get_object_or_404(Accommodation,id=accommodation_id)

    if request.method == 'POST':
        frmAccommodation = AccommodationForm(request.POST,request.FILES,instance=accommodation)
        if frmAccommodation.is_valid():
            frmAccommodation.save()
            return redirect("/")
    else:
        frmAccommodation = AccommodationForm(instance=accommodation)
    
    context = {
        "fmrAccomodation":frmAccommodation
    }
    
    return render(request,'asa_travel/edit_accommodation.html',context)

def edit_activity(request,activity_id):
    activity = get_object_or_404(ActivityAndTour,id=activity_id)

    if request.method == 'POST':
        frmActivity = ActivityForm(request.POST,request.FILES,instance=activity)
        if frmActivity.is_valid():
            frmActivity.save()
            return redirect("/")
    else:
        frmActivity = ActivityForm(instance=activity)
    
    context = {
        "frmActivity":frmActivity
    }

    return render(request,'asa_travel/edit_activity.html',context)

"""VISTAS ADMIN ELIMINACION"""

def delete_review(request,review_id):
    review = get_object_or_404(Review,id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')

def delete_attraction(request,attraction_id):
    attraction = get_object_or_404(Attraction,id=attraction_id)

    if request.method == 'POST':
        attraction.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')

def delete_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(FoodAndRestaurant,id=restaurant_id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')

def delete_accommodation(request,accommodation_id):
    accommodation = get_object_or_404(Accommodation,id=accommodation_id)

    if request.method == 'POST':
        accommodation.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')

def delete_activity(request,activity_id):
    activity = get_object_or_404(ActivityAndTour,id=activity_id)

    if request.method == 'POST':
        activity.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')
