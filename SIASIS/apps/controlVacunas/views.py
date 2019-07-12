from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import datetime
from apps.controlVacunas.models import Vacuna
from apps.controlVacunas.models import ControlVacuna
from apps.controlVacunas.forms import ControlVacuForm
from apps.controlVacunas.forms import VacuForm
from apps.registroMascota.models import Expediente


def index_vacu(request,x):
    edicion = False
    vacu = ControlVacuna.objects.filter(expediente=x).order_by('id')
    ultVacu = ControlVacuna.objects.filter(expediente=x).order_by('id').last()
    expediente=Expediente.objects.get(id=x)
    if request.method == "POST":  
        form = ControlVacuForm(request.POST)  
        if form.is_valid():  
            try:                  
                instance = form.save(commit=False) 
                instance.expediente = expediente
                instance.save()
                return HttpResponseRedirect(reverse('controlVacunas:index_vacu2', kwargs={'x':x}))  
            except:  
                pass  
    else:  
        form = ControlVacuForm()   
    return render(request,'controlVacunas/index_vacuna.html',{'varvacu':vacu,'form':form, 'edicion':edicion, 'idmasc':expediente,'ultVacu':ultVacu})

def registrar_vacu(request):
	if request.method == 'POST':
		form=ControlVacuForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect(reverse('controlVacunas:index_vacu2',kwargs={'x':x}))
	else:
		form=ControlVacuForm()
	return render(request,'controlVacunas/registrar_vacuna.html',{'form':form})

def editar_vacu(request, x, num):
    edicion = True
    vacunas = ControlVacuna.objects.filter(expediente=x).order_by('id')
    instancia = ControlVacuna.objects.get(id=num)
    expediente=Expediente.objects.get(id=x)
    if request.method=='GET':
        form=ControlVacuForm(instance=instancia)
    else:
        form=ControlVacuForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            form = ControlVacuForm()
            return redirect(reverse('controlVacunas:index_vacu2',kwargs={'x':x}))
    return render(request,'controlVacunas/index_vacuna.html', {'varvacunas':vacunas,'form':form,'edicion':edicion,'idmasc':expediente})

def eliminar_vacu(request, x, num):  
    vacu = ControlVacuna.objects.filter(expediente=x).get(id=num) 
    vacu.delete()  
    return redirect(reverse('controlVacunas:index_vacu2',kwargs={'x':x}))

def nueva_vacu(request,x):
    if request.method=='POST':
        form=VacuForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('controlVacunas:index_vacu2',kwargs={'x':x}))
    else:
        form=VacuForm()
    return render(request, 'controlVacunas/nueva_vacu.html', {'form':form,'idmasc':x})

def index_vacu3(request):
    edicion = False
    vacu = ControlVacuna.objects.all().order_by('id')
    if request.method == "POST":  
        form = ControlVacuForm(request.POST)  
        if form.is_valid():  
            try:
                form.save()           
                return HttpResponseRedirect(reverse('controlVacunas:index_vacu3'))  
            except:  
                pass  
    else:  
        form = ControlVacuForm()   
    return render(request,'controlVacunas/index_vacuna.html',{'varvacu':vacu,'form':form, 'edicion':edicion})

