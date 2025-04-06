from django.contrib import admin
from .models import Accommodation,ActivityAndTour,\
                    Attraction,Category,Destination,FoodAndRestaurant
# Register your models here.
admin.site.register(Accommodation)
admin.site.register(Destination)
admin.site.register(ActivityAndTour)
admin.site.register(Attraction)
admin.site.register(Category)
admin.site.register(FoodAndRestaurant)
