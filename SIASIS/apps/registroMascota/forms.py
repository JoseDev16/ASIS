from django import forms

from apps.registroMascota.models import Mascota

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
            'fechaNacimiento': forms.SelectDateWidget,
            'razaPadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'razaMadre': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'peso': forms.TextInput(attrs={'class': 'input','size' : 30}),
        }