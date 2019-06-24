from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from apps.controlVacunas.models import Vacuna
from apps.controlVacunas.models import ControlVacuna
from apps.controlVacunas.forms import ControlVacuForm
from apps.controlVacunas.forms import VacuForm

def index_vacu(request):
    edicion = False
    vacu = ControlVacuna.objects.all()
    
    if request.method == "POST":  
        form = ControlVacuForm(request.POST)  
        if form.is_valid():  
            try:                  
                form.save()  
                form = ControlVacuForm()
                return HttpResponseRedirect(reverse('controlVacu:index_vacu'))  
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
		return redirect('controlVacu:index_vacu')
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
			return redirect('controlVacu:index_vacu')
	return render(request,'controlVacunas/registrar_vacuna.html', {'form':form})

def eliminar_vacu(request, num):  
    vacu = ControlVacuna.objects.get(id=num) 
    if request.method=='POST':
    	vacu.delete()  
    	return redirect('controlVacu:index_vacu')
    return render(request,'controlVacunas/eliminar_vacuna.html',{'vacu':vacu})

def nueva_vacu(request):
    if request.method=='POST':
        form=VacuForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('controlVacu:index_vacu')
    else:
        form=VacuForm()
    return render(request, 'controlVacunas/nueva_vacu.html', {'form':form})

