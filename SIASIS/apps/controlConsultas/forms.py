from django import forms
from apps.controlConsultas.models import Consulta
from datetime import datetime
from datetime import date


ahora=date.today()
año=ahora.year
mes=ahora.month
dia=ahora.day
class ConsultaForm(forms.ModelForm):
    class Meta:
        model=Consulta

        fields = [
            'titulo',
            'detalleConsulta',
            'medicamento',
            'proximaCita',
            'citaunica',

        ]

        labels = {
            'titulo': 'Titulo',
            'detalleConsulta': 'Detalles y Sintomas',
            'medicamento': 'Tratamiento',
            'proximaCita': 'Proxima cita',
            'citaunica': 'Cita unica',

        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control','size' : 30}),
            'medicamento': forms.TextInput(attrs={'class':'form-control','size' : 30,'rows':3}),
            'detalleConsulta': forms.Textarea(attrs={'class': 'form-control','size' : 30}),

            'proximaCita': forms.TextInput(attrs={'type':'date','min':ahora}),
            'citaunica': forms.CheckboxInput(attrs={'class': 'input'}),
            
        }