from django.shortcuts import render
from django.urls import reverse
from apps.controlCelo.models import ControlCelo
from apps.controlCelo.models import Celo
from apps.controlCelo.forms import CeloForm
from apps.controlCelo.forms import ControlCeloForm
from apps.registroMascota.models import Expediente
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import datetime

# Create your views here.

def index_celo(request,x):
    edicion = False
    celos = ControlCelo.objects.filter(expediente=x).order_by('id')
    expediente=Expediente.objects.get(id=x)
    if request.method == "POST":  
        form = ControlCeloForm(request.POST)  
        if form.is_valid():  
            try:
                instance = form.save(commit=False) 
                instance.expediente = expediente
                instance.save()
                return HttpResponseRedirect(reverse('controlCelo:index-celo', kwargs={'x':x}))  
            except Exception as e:   
                form = ControlCeloForm() 
                pass
    else:  
        form = ControlCeloForm()   
    return render(request,'controlCelo/index_celo.html',{'varcelos':celos,'form':form, 'edicion':edicion, 'idmasc':expediente.id})
    
def registrar_vacuna(request,n):
    if request.method == "POST":  
        x = CeloForm(request.POST)  
        if x.is_valid():  
            try:  
                x.save()  
                return HttpResponseRedirect(reverse('controlCelo:index-celo', kwargs={'x':x})) 
            except:  
                pass  
    else:  
        x = CeloForm()   
    return render(request,'controlCelo/registrar_vacuna_celo.html',{'form':x})
    
def editar_celo(request,x,num):
    edicion = True
    celos = ControlCelo.objects.filter(expediente=x).order_by('id')
    instancia = ControlCelo.objects.get(id=num)
    expediente=Expediente.objects.get(id=x)
    if request.method == "POST":
        form = ControlCeloForm(request.POST,instance=instancia) 
        if form.is_valid():  
            try:                  
                form.save()  
                form = ControlCeloForm()
                return HttpResponseRedirect(reverse('controlCelo:index-celo', kwargs={'x':x})) 
            except:
                pass
    else:
        form=ControlCeloForm(instance=instancia)
    return render(request,'controlCelo/index_celo.html',{'varcelos':celos, 'form':form, 'edicion':edicion,'idmasc':expediente.id})
    
def eliminar_celo(request,x,num):  
    valor = ControlCelo.objects.filter(expediente=x).get(id=num)  
    valor.delete()  
    return HttpResponseRedirect(reverse('controlCelo:index-celo', kwargs={'x':x}))