from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='destination',blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=70)
    status = models.BooleanField()

    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    opening_hours = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class FoodAndRestaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=50)
    price_range = models.CharField(max_length=10)
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodation_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class ActivityAndTour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    available_dates = models.CharField(max_length=100)

    def __str__(self):
        return self.name
