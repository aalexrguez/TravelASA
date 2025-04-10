from django import forms
from .models import Destination,Review

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
