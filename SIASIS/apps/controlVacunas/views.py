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
    expediente=Expediente.objects.get(id=x)
    
    if request.method == "POST":  
        form = ControlVacuForm(request.POST)  
        if form.is_valid():  
            try:                  
                instance = form.save(commit=False) 
                instance.expediente = expediente
                instance.save()
                return HttpResponseRedirect(reverse('controlVacunas:index_vacu', kwargs={'x':x}))  
            except:  
                pass  
    else:  
        form = ControlVacuForm()   
    return render(request,'controlVacunas/index_vacuna.html',{'varvacu':vacu,'form':form, 'edicion':edicion})

def registrar_vacu(request):
	if request.method == 'POST':
		form=ControlVacuForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('controlVacunas:index_vacu3')
	else:
		form=ControlVacuForm()
	return render(request,'controlVacunas/registrar_vacuna.html',{'form':form})

def editar_vacu(request, num):
	vacuna=ControlVacuna.objects.get(id=num)
	if request.method=='GET':
		form=ControlVacuForm(instance=vacuna)
	else:
		form=ControlVacuForm(request.POST, instance=vacuna)
		if form.is_valid():
			form.save()
			return redirect('controlVacunas:index_vacu3')
	return render(request,'controlVacunas/registrar_vacuna.html', {'form':form})

def eliminar_vacu(request, num):  
    vacu = ControlVacuna.objects.get(id=num) 
    if request.method=='POST':
    	vacu.delete()  
    	return redirect('controlVacunas:index_vacu3')
    return render(request,'controlVacunas/eliminar_vacuna.html',{'vacu':vacu})

def nueva_vacu(request):
    if request.method=='POST':
        form=VacuForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('controlVacunas:index_vacu3')
    else:
        form=VacuForm()
    return render(request, 'controlVacunas/nueva_vacu.html', {'form':form})

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

