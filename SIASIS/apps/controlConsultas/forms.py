from django import forms
from apps.controlConsultas.models import Consulta

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
            'detalleConsulta': 'Detalles',
            'medicamento': 'tratamiento',
            'proximaCita': 'Seguimiento',
            'citaunica': 'Cita unica',

        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'detalle consulta': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'medicamento': forms.TextInput(attrs={'class': 'input','size' : 30}),
            'proximacita': forms.TextInput(attrs={'class':'input','type':'date'}),
            'citaunica': forms.TextInput(attrs={'class': 'input','size' : 30}),
            
        }