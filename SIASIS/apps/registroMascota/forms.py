from django import forms

from apps.registroMascota.models import Mascota, DueñoMascota
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

class CuentaForm(UserCreationForm):

	class Meta:
		model=User
		fields = [
			'username',
			'first_name',
			'last_name',
			
		]
		labels={
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name':'Apellido',
			
		}

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota

        fields = [
            'nombre',
            'raza',
            'sexo',
            'fechaNacimiento',
            'razaPadre',
            'razaMadre',
            'peso',
        ]

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'fechaNacimiento': 'Fecha de nacimiento',
            'razaPadre': 'Raza del padre',
            'razaMadre': 'Raza de la madre',
            'peso': 'Peso (kg)',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'raza': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'sexo': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'fechaNacimiento': forms.DateInput(attrs={'type':'date','max':datetime.now().date}),
            'razaPadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'razaMadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'peso': forms.TextInput(attrs={'class': 'input','size' : 30}),
        }

class DueñoMascotaForm(forms.ModelForm):
    class Meta: 
        model =DueñoMascota

        
        fields = [

            
            'direccion',
            'telefono',
            'celular',
            
        ]

        labels = {

            
            'direccion': 'Direccion',
            'telefono': 'Telefono de casa',
            'celular': 'celular',
            
        }

        widgets = {

            'direccion': forms.TextInput(attrs={'class': 'input','size' : 30}),
           
            'telefono': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'celular': forms.TextInput(attrs={'class': 'input','size' : 30}),
            
        }

