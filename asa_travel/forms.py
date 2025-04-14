from django import forms
from .models import Destination,Review
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

class AttractionForm(forms.Form):
    attraction_name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    attraction_description = forms.CharField(
        label='Descripción',
        max_length=150,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    attraction_destination = forms.ModelChoiceField(
        queryset=Destination.objects.all(),
        label='Destino',
        empty_label='Selecciona un destino',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    attraction_category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoría',
        empty_label='Selecciona una categoría',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    attraction_opening_hours = forms.CharField(
        label='Horario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    attraction_price = forms.DecimalField(
        label='Precio',
        max_digits=7,
        decimal_places=2,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    attraction_image = forms.ImageField(label='Imagen', required=False)
    attraction_website = forms.URLField(label='Sitio Web', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    attraction_map_url = forms.CharField(label='Mapa (URL)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    attraction_rating = forms.IntegerField(
        label='Calificación (1-5)',
        required=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

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

class RestaurantForm(forms.Form):
    fd_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fd_description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    fd_destination = forms.ModelChoiceField(queryset=Destination.objects.all(), label='Destino', widget=forms.Select(attrs={'class': 'form-select'}))
    fd_food_type = forms.CharField(label='Tipo de Comida', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fd_price_range = forms.CharField(label='Rango de Precio', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fd_opening_hours = forms.CharField(label='Horario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fd_image = forms.ImageField(label='Imagen', required=False)
    fd_website = forms.URLField(label='Sitio Web', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    fd_map_url = forms.CharField(label='Mapa (URL)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    fd_rating = forms.IntegerField(label='Calificación (1-5)', required=False, validators=[MinValueValidator(1), MaxValueValidator(5)], widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_fd_price_range(self):
        rango = self.cleaned_data['fd_price_range']
        if not '-' in rango:
            raise forms.ValidationError('El rango debe tener el formato mínimo-máximo, por ejemplo: 50-100.')
        return rango

    def clean_fd_description(self):
        desc = self.cleaned_data['fd_description']
        if len(desc.strip()) < 10:
            raise forms.ValidationError('La descripción es muy corta.')
        return desc

class AccommodationForm(forms.Form):
    accommodation_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    accommodation_description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    accommodation_destination = forms.ModelChoiceField(queryset=Destination.objects.all(), label='Destino', widget=forms.Select(attrs={'class': 'form-select'}))
    accommodation_type = forms.CharField(label='Tipo', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    accommodation_price_per_night = forms.DecimalField(label='Precio por noche', max_digits=7, decimal_places=2, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    accommodation_image = forms.ImageField(label='Imagen', required=False)
    accommodation_website = forms.URLField(label='Sitio Web', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    accommodation_map_url = forms.CharField(label='Mapa (URL)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    accommodation_rating = forms.IntegerField(label='Calificación (1-5)', required=False, validators=[MinValueValidator(1), MaxValueValidator(5)], widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_accommodation_description(self):
        desc = self.cleaned_data['accommodation_description']
        if len(desc.split()) < 5:
            raise forms.ValidationError('La descripción debe tener al menos 5 palabras.')
        return desc

class ActivityForm(forms.Form):
    at_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    at_description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    at_destination = forms.ModelChoiceField(queryset=Destination.objects.all(), label='Destino', widget=forms.Select(attrs={'class': 'form-select'}))
    at_duration = forms.CharField(label='Duración', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    at_price = forms.DecimalField(label='Precio', max_digits=7, decimal_places=2, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    at_available_dates = forms.CharField(label='Fechas Disponibles', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    at_image = forms.ImageField(label='Imagen', required=False)
    at_website = forms.URLField(label='Sitio Web', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    at_map_url = forms.CharField(label='Mapa (URL)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    at_rating = forms.IntegerField(label='Calificación (1-5)', required=False, validators=[MinValueValidator(1), MaxValueValidator(5)], widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_at_available_dates(self):
        dates = self.cleaned_data['at_available_dates']
        if len(dates.strip()) < 5:
            raise forms.ValidationError('Debes ingresar al menos una fecha válida.')
        return dates

