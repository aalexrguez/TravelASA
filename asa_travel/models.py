from django.db import models

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
        return self.name

class Attraction(models.Model):
    attraction_name = models.CharField(max_length=100)
    attraction_description = models.CharField(max_length=150)
    attraction_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    attraction_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    attraction_opening_hours = models.CharField(max_length=50)
    attraction_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.attraction_name

class FoodAndRestaurant(models.Model):
    fd_name = models.CharField(max_length=100)
    fd_description = models.TextField()
    fd_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    fd_food_type = models.CharField(max_length=50)
    fd_price_range = models.CharField(max_length=10)
    fd_opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.fd_name

class Accommodation(models.Model):
    accommodation_name = models.CharField(max_length=100)
    accommodation_description = models.TextField()
    accommodation_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodation_type = models.CharField(max_length=50)
    accommodation_price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    accommodation_rating = models.FloatField()

    def __str__(self):
        return self.accommodation_name

class ActivityAndTour(models.Model):
    at_name = models.CharField(max_length=100)
    at_description = models.TextField()
    at_destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    at_duration = models.CharField(max_length=50)
    at_price = models.DecimalField(max_digits=7, decimal_places=2)
    at_available_dates = models.CharField(max_length=100)

    def __str__(self):
        return self.at_name
