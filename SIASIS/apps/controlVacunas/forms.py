from django import forms
from apps.controlVacunas.models import ControlVacuna
from apps.controlVacunas.models import Vacuna

class ControlVacuForm(forms.ModelForm):
    class Meta:

        model = ControlVacuna
        
        fields = [
            'fechaAplicacionVac',
            
            'fechaProxVac',
            'cantDosis',
            'vacu',

        ]
        labels={
            'fechaAplicacionVac':'Fecha de aplicacion',
            
            'fechaProxVac':'Fecha de la siguiente vacunacion',
            'cantDosis': 'Dosis',
            'vacu':'Nombre',
        }
        
        widgets = {
            'fechaAplicacionVac' : forms.SelectDateWidget,
            
            'fechaProxVac' : forms.SelectDateWidget,
            'cantDosis' : forms.TextInput(attrs={'class':'form-control'}),
            'vacu': forms.Select(attrs={'class':'form-control'}),
             
            }
class VacuForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields=['nombre']