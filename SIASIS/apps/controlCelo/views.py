from django.shortcuts import render
from django.urls import reverse
from apps.controlCelo.models import ControlCelo
from apps.controlCelo.models import Celo
from apps.controlCelo.forms import CeloForm
from apps.controlCelo.forms import ControlCeloForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import datetime

# Create your views here.

def index_celo(request):
    edicion = False
    celos = ControlCelo.objects.all()
    #ControlCelo.objects.all().delete()
    #Celo.objects.all().delete()
    if request.method == "POST":  
        form = ControlCeloForm(request.POST)  
        if form.is_valid():  
            try:                  
                form.save()  
                form = ControlCeloForm()
                return HttpResponseRedirect(reverse('controlCelo:index-celo'))  
            except:  
                pass  
    else:  
        form = ControlCeloForm()   
    return render(request,'controlCelo/index_celo.html',{'varcelos':celos,'form':form, 'edicion':edicion})
    
def registrar_vacuna(request):
    if request.method == "POST":  
        x = CeloForm(request.POST)  
        if x.is_valid():  
            try:  
                x.save()  
                return HttpResponseRedirect(reverse('controlCelo:index-celo')) 
            except:  
                pass  
    else:  
        x = CeloForm()   
    return render(request,'controlCelo/registrar_vacuna_celo.html',{'form':x})
    
def editar_celo(request,num):
    edicion = True
    celos = ControlCelo.objects.all()
    instancia = ControlCelo.objects.get(id=num)
    if request.method == "POST":
        form = ControlCeloForm(request.POST,instance=instancia) 
        if form.is_valid():  
            try:                  
                form.save()  
                form = ControlCeloForm()
                return HttpResponseRedirect(reverse('controlCelo:index-celo')) 
            except:
                pass
    else:
        form=ControlCeloForm(instance=instancia)
    return render(request,'controlCelo/index_celo.html',{'varcelos':celos, 'form':form, 'edicion':edicion})
    
def eliminar_celo(request, num):  
    valor = ControlCelo.objects.get(id=num)  
    valor.delete()  
    return redirect('controlCelo:index-celo')