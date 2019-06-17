from django import forms
from apps.controlCelo.models import ControlCelo
from apps.controlCelo.models import Celo
class ControlCeloForm(forms.ModelForm):
    class Meta:
        model = ControlCelo
        fields=['fechaInicioCelo','fechaFinCelo','fechaAplic','celo']
        widgets = {
            'fechaInicioCelo' : forms.SelectDateWidget,
            'fechaFinCelo' : forms.SelectDateWidget,
            'fechaAplic' : forms.SelectDateWidget,
        #    'celo': forms.ModelChoiceField(queryset=Celo.objects.all(),empty_label="ninguna"),
        }
        
class CeloForm(forms.ModelForm):
    class Meta:
        model = Celo
        fields=['nombreVacunaCelo']
