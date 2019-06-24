from django import forms
import datetime
from apps.controlCelo.models import ControlCelo
from apps.controlCelo.models import Celo
class ControlCeloForm(forms.ModelForm):
    class Meta:
        model = ControlCelo
        fields=['fechaInicioCelo','fechaFinCelo','fechaAplic','celo', 'proximoCelo']
        widgets = {
            'fechaInicioCelo' : forms.DateInput(attrs={'type':'date','max':datetime.datetime.now().strftime('%Y-%m-%d'), 'value':datetime.datetime.now().strftime('%Y-%m-%d')}),
            'fechaFinCelo' : forms.DateInput(attrs={'type':'date', 'value':datetime.datetime.now().strftime('%Y-%m-%d')}),
            'fechaAplic' : forms.DateInput(attrs={'type':'date','max':datetime.datetime.now().strftime('%Y-%m-%d'), 'value':datetime.datetime.now().strftime('%Y-%m-%d')}),
            'proximoCelo' : forms.DateInput(attrs={'type':'date','min':datetime.datetime.now().strftime('%Y-%m-%d'), 'value':datetime.datetime.now().strftime('%Y-%m-%d')}),
            #'expediente': forms.HiddenInput(),
        }
        
class CeloForm(forms.ModelForm):
    class Meta:
        model = Celo
        fields=['nombreVacunaCelo']