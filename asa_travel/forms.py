from django import forms
from .models import Destination,Review,Category,Attraction\
    ,FoodAndRestaurant,Accommodation,ActivityAndTour
from django.core.validators import MinValueValidator, MaxValueValidator

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientForm(forms.Form):
    client_sex = forms.CharField(label='Sexo')
    client_phone = forms.CharField(label='Telefono')
    client_date_of_birth = forms.DateField(label='Fecha de nacimiento',input_formats=['%Y-%m-%d'],widget=DateInput)
    client_image = forms.ImageField(label='Imagen')

class ReviewForm(forms.Form):
    destination = forms.ModelChoiceField(
        queryset=Destination.objects.all(),
        label='Destino',
        empty_label='Selecciona un destino'
    )
    comment = forms.CharField(
        label='Reseña',
        widget=forms.Textarea
    )
    rating = forms.ChoiceField(
        label='Calificación',
        choices=Review.RATING_CHOICES
    )

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = [
            'attraction_name',
            'attraction_description',
            'attraction_destination',
            'attraction_category',
            'attraction_opening_hours',
            'attraction_price',
            'attraction_image',
            'attraction_website',
            'attraction_map_url',
            'attraction_rating'
        ]
        labels = {
            'attraction_name': 'Nombre',
            'attraction_description': 'Descripción',
            'attraction_destination': 'Destino',
            'attraction_category': 'Categoría',
            'attraction_opening_hours': 'Horario',
            'attraction_price': 'Precio',
            'attraction_image': 'Imagen',
            'attraction_website': 'Sitio Web',
            'attraction_map_url': 'Mapa (URL)',
            'attraction_rating': 'Calificación (1-5)'
        }
        widgets = {
            'attraction_name': forms.TextInput(attrs={'class': 'form-control'}),
            'attraction_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'attraction_destination': forms.Select(attrs={'class': 'form-select'}),
            'attraction_category': forms.Select(attrs={'class': 'form-select'}),
            'attraction_opening_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'attraction_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'attraction_website': forms.URLInput(attrs={'class': 'form-control'}),
            'attraction_map_url': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'attraction_rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_attraction_name(self):
        name = self.cleaned_data['attraction_name']
        if len(name) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return name

    def clean_attraction_description(self):
        desc = self.cleaned_data['attraction_description']
        if len(desc.split()) < 5:
            raise forms.ValidationError('La descripción debe contener al menos 5 palabras.')
        return desc

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = FoodAndRestaurant
        fields = [
            'fd_name',
            'fd_description',
            'fd_destination',
            'fd_food_type',
            'fd_price_range',
            'fd_opening_hours',
            'fd_image',
            'fd_website',
            'fd_map_url',
            'fd_rating'
        ]
        labels = {
            'fd_name': 'Nombre',
            'fd_description': 'Descripción',
            'fd_destination': 'Destino',
            'fd_food_type': 'Tipo de Comida',
            'fd_price_range': 'Rango de Precio',
            'fd_opening_hours': 'Horario',
            'fd_image': 'Imagen',
            'fd_website': 'Sitio Web',
            'fd_map_url': 'Mapa (URL)',
            'fd_rating': 'Calificación (1-5)',
        }
        widgets = {
            'fd_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fd_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fd_destination': forms.Select(attrs={'class': 'form-select'}),
            'fd_food_type': forms.TextInput(attrs={'class': 'form-control'}),
            'fd_price_range': forms.TextInput(attrs={'class': 'form-control'}),
            'fd_opening_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'fd_website': forms.URLInput(attrs={'class': 'form-control'}),
            'fd_map_url': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fd_rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_fd_description(self):
        desc = self.cleaned_data['fd_description']
        if len(desc.strip()) < 10:
            raise forms.ValidationError('La descripción es muy corta.')
        return desc


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = [
            'accommodation_name',
            'accommodation_description',
            'accommodation_destination',
            'accommodation_type',
            'accommodation_price_per_night',
            'accommodation_image',
            'accommodation_website',
            'accommodation_map_url',
            'accommodation_rating',
        ]
        labels = {
            'accommodation_name': 'Nombre',
            'accommodation_description': 'Descripción',
            'accommodation_destination': 'Destino',
            'accommodation_type': 'Tipo',
            'accommodation_price_per_night': 'Precio por noche',
            'accommodation_image': 'Imagen',
            'accommodation_website': 'Sitio Web',
            'accommodation_map_url': 'Mapa (URL)',
            'accommodation_rating': 'Calificación (1-5)',
        }
        widgets = {
            'accommodation_name': forms.TextInput(attrs={'class': 'form-control'}),
            'accommodation_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'accommodation_destination': forms.Select(attrs={'class': 'form-select'}),
            'accommodation_type': forms.TextInput(attrs={'class': 'form-control'}),
            'accommodation_price_per_night': forms.NumberInput(attrs={'class': 'form-control'}),
            'accommodation_website': forms.URLInput(attrs={'class': 'form-control'}),
            'accommodation_map_url': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'accommodation_rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_accommodation_description(self):
        desc = self.cleaned_data['accommodation_description']
        if len(desc.split()) < 5:
            raise forms.ValidationError('La descripción debe tener al menos 5 palabras.')
        return desc


class ActivityForm(forms.ModelForm):
    class Meta:
        model = ActivityAndTour
        fields = [
            'at_name',
            'at_description',
            'at_destination',
            'at_duration',
            'at_price',
            'at_available_dates',
            'at_image',
            'at_website',
            'at_map_url',
            'at_rating'
        ]
        labels = {
            'at_name': 'Nombre',
            'at_description': 'Descripción',
            'at_destination': 'Destino',
            'at_duration': 'Duración',
            'at_price': 'Precio',
            'at_available_dates': 'Fechas Disponibles',
            'at_image': 'Imagen',
            'at_website': 'Sitio Web',
            'at_map_url': 'Mapa (URL)',
            'at_rating': 'Calificación (1-5)',
        }
        widgets = {
            'at_name': forms.TextInput(attrs={'class': 'form-control'}),
            'at_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'at_destination': forms.Select(attrs={'class': 'form-select'}),
            'at_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'at_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'at_available_dates': forms.TextInput(attrs={'class': 'form-control'}),
            'at_website': forms.URLInput(attrs={'class': 'form-control'}),
            'at_map_url': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'at_rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_at_description(self):
        desc = self.cleaned_data['at_description']
        if len(desc.strip().split()) < 5:
            raise forms.ValidationError('La descripción debe tener al menos 5 palabras.')
        return desc


