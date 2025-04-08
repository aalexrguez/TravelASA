from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class ClientForm(forms.Form):
    client_first_name = forms.CharField(label='Nombre')
    client_last_name = forms.CharField(label='Apellido')
    client_email = forms.CharField(label='Email')
    client_sex = forms.CharField(label='Sexo')
    client_phone = forms.CharField(label='Telefono')
    client_date_of_birth = forms.DateField(label='Fecha de nacimiento',input_formats=['%Y-%m-%d'],widget=DateInput)
    client_image = forms.ImageField(label='Imagen')
