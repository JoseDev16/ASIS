from django import forms
from apps.controlDesp.models import ControlDesparasitacion
from apps.controlDesp.models import Desparasitante

class ControlDesparasitacionForm(forms.ModelForm):
    class Meta:

        model = ControlDesparasitacion
        
        fields = [
            'fechaAplicacion',
            'fechaProxDes', 
            'dosisDesp', 
            'desparasitante', 
            
        ]
        labels={
            'fechaAplicacion': 'Fecha aplicacion',
            'fechaProxDes':'Fecha proxima desparasitacion',
            'dosisDesp':'Dosis',
            'desparasitante':'Desparasitante',
        }
        
        widgets = {
            'fechaAplicacion' : forms.SelectDateWidget,
            'fechaProxDes' : forms.SelectDateWidget,
            'dosisDesp' : forms.TextInput(attrs={'class':'form-control'}),
            'desparasitante': forms.Select(attrs={'class':'form-control'}),
             
            }
class DespForm(forms.ModelForm):
    class Meta:
        model = Desparasitante
        fields=['nombreDesparasitante']