from django import forms

from apps.registroMascota.models import Mascota, DueñoMascota
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from datetime import date

ahora=date.today()
año=ahora.year
mes=ahora.month
dia=ahora.day

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
            'dueñomascota',
        ]

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'fechaNacimiento': 'Fecha de nacimiento',
            'razaPadre': 'Raza del padre',
            'razaMadre': 'Raza de la madre',
            'peso': 'Peso (kg)',
            'dueñomascota':'Dueño de la mascota',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'raza': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'sexo': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'fechaNacimiento': forms.TextInput(attrs={'type':'date','max':ahora}),
            'razaPadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'razaMadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'peso': forms.NumberInput(attrs={'class': 'input','min': '0.00','step':'0.1','size' : 30}),
            'dueñomascota':forms.Select(attrs={'class':'form-control','width':30}),
        }

class DueñoMascotaForm(forms.ModelForm):
    class Meta: 
        model =DueñoMascota

        
        fields = [

            
            'direccion',
            'telefono',
            'celular',
            'fechaNacDueno',
            'correo',
            
        ]

        labels = {

            
            'direccion': 'Direccion',
            'telefono': 'Telefono de casa',
            'celular': 'celular',
            'fechaNacDueno': 'Fecha de nacimiento',
            'correo': 'Correo electrónico',
            
        }

        widgets = {

            'direccion': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'telefono': forms.NumberInput(attrs={'class': 'input','size' : 30}),
            'celular': forms.NumberInput(attrs={'class': 'input','size' : 30}),
            'fechaNacDueno':forms.TextInput(attrs={'class':'input','type':'date',
                'value':(date((ahora.year)-18,mes,dia)),'max':(date((ahora.year)-18,mes,dia))}),
            'correo':forms.EmailInput(),
            
        }

