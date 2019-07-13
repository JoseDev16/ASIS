from django.shortcuts import render
from django.urls import reverse
from apps.controlDesp.models import ControlDesparasitacion
from apps.controlDesp.models import Desparasitante
from apps.controlDesp.forms import DespForm
from apps.controlDesp.forms import ControlDesparasitacionForm
from apps.registroMascota.models import Expediente
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import datetime

# Create your views here.

def index_desparasitacion(request,x):
    edicion = False
    desparasitaciones = ControlDesparasitacion.objects.filter(expediente=x).order_by('id')
    ultDesparasitante = ControlDesparasitacion.objects.filter(expediente=x).order_by('id').last()
    expediente=Expediente.objects.get(id=x)
    if request.method == "POST":  
        form = ControlDesparasitacionForm(request.POST)  
        if form.is_valid():  
            try:
                instance = form.save(commit=False) 
                instance.expediente = expediente
                instance.save()
                return HttpResponseRedirect(reverse('controlDesp:index-desparasitacion', kwargs={'x':x}))  
            except Exception as e:   
                form = ControlDesparasitacionForm() 
                pass
    else:  
        form = ControlDesparasitacionForm()   
    return render(request,'controlDesp/index_desp.html',{'vardesparasitante':desparasitaciones,'form':form, 'edicion':edicion, 'idmasc':expediente, 'ultDesparasitante':ultDesparasitante})
    
def registrar_vacuna(request,x):
    if request.method == "POST":  
        form = DespForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponseRedirect(reverse('controlDesp:index-desparasitacion', kwargs={'x':x})) 
            except:  
                pass  
    else:  
        form = DespForm()   
    return render(request,'controlDesp/nuevo_desp.html',{'form':form, 'idmasc':x})
    
def editar_desparasitacion(request,x,num):
    edicion = True
    desparasitaciones = ControlDesparasitacion.objects.filter(expediente=x).order_by('id')
    instancia = ControlDesparasitacion.objects.get(id=num)
    expediente=Expediente.objects.get(id=x)
    if request.method == "POST":
        form = ControlDesparasitacionForm(request.POST,instance=instancia) 
        if form.is_valid():  
            try:                  
                form.save()  
                form = ControlDesparasitacionForm()
                return HttpResponseRedirect(reverse('controlDesp:index-desparasitacion', kwargs={'x':x})) 
            except:
                pass
    else:
        form=ControlDesparasitacionForm(instance=instancia)
    return render(request,'controlDesp/index_desp.html',{'vardesparasitante':desparasitaciones, 'form':form, 'edicion':edicion,'idmasc':expediente})
    
def eliminar_desparasitacion(request,x,num):  
    valor = ControlDesparasitacion.objects.filter(expediente=x).get(id=num)  
    valor.delete()  
    return HttpResponseRedirect(reverse('controlDesp:index-desparasitacion', kwargs={'x':x}))
