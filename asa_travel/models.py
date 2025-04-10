from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Destination(models.Model):
    destination_name = models.CharField(max_length=80, unique=True)
    destination_description = models.CharField(max_length=255)
    destination_image = models.ImageField(upload_to='destination',blank=True)

    def __str__(self):
        return self.destination_name

class Category(models.Model):
    category_name = models.CharField(max_length=70)
    category_status = models.BooleanField()

    def __str__(self):
        return self.category_name

class Attraction(models.Model):
    attraction_name = models.CharField(max_length=100)
    attraction_description = models.CharField(max_length=150)
    attraction_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    attraction_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    attraction_opening_hours = models.CharField(max_length=50)
    attraction_price = models.DecimalField(max_digits=7, decimal_places=2)
    attraction_image = models.ImageField(upload_to='attraction',blank=True)
    attraction_website = models.URLField(blank=True, null=True)
    attraction_map_url = models.TextField(blank=True, null=True)
    attraction_rating = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.attraction_name

class FoodAndRestaurant(models.Model):
    fd_name = models.CharField(max_length=100)
    fd_description = models.TextField()
    fd_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    fd_food_type = models.CharField(max_length=50)
    fd_price_range = models.CharField(max_length=10)
    fd_opening_hours = models.CharField(max_length=50)
    fd_image = models.ImageField(upload_to='foodRestaurant',blank=True)
    fd_website = models.URLField(blank=True, null=True)
    fd_map_url = models.TextField(blank=True, null=True)
    fd_rating = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.fd_name

class Accommodation(models.Model):
    accommodation_name = models.CharField(max_length=100)
    accommodation_description = models.TextField()
    accommodation_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodation_type = models.CharField(max_length=50)
    accommodation_price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    accommodation_rating = models.FloatField()
    accommodation_image = models.ImageField(upload_to='accommodation',blank=True)
    accommodation_website = models.URLField(blank=True, null=True)
    accommodation_map_url = models.TextField(blank=True, null=True)
    accommodation_rating = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.accommodation_name

class ActivityAndTour(models.Model):
    at_name = models.CharField(max_length=100)
    at_description = models.TextField()
    at_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    at_duration = models.CharField(max_length=50)
    at_price = models.DecimalField(max_digits=7, decimal_places=2)
    at_available_dates = models.CharField(max_length=100)
    at_image = models.ImageField(upload_to='activity',blank=True)
    at_website = models.URLField(blank=True, null=True)
    at_map_url = models.TextField(blank=True, null=True)
    at_rating = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.at_name


class Client(models.Model):
    SEX_CHOICES = (
        ('M','MASCULINO'),
        ('F','FEMENINO')
    )
    client_user = models.OneToOneField(User,on_delete = models.RESTRICT)
    client_sex = models.CharField(max_length=1,choices=SEX_CHOICES,default='M')
    client_phone = models.CharField(max_length=20)
    client_date_of_birth = models.DateField(null=True)
    client_image = models.ImageField(upload_to='client',blank=True)

    def __str__(self):
        return self.client_user.username

class Review(models.Model):

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    review_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    review_destination = models.ForeignKey(Destination,on_delete=models.RESTRICT)
    review_comment = models.TextField()
    review_rating = models.IntegerField(choices=RATING_CHOICES)
    review_create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.review_user.username + self.review_destination.destination_name

