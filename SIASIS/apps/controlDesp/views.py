from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from apps.controlDesp.models import Desparasitante
from apps.controlDesp.models import ControlDesparasitacion
from apps.controlDesp.forms import ControlDesparasitacionForm
from apps.controlDesp.forms import DespForm

def index_desp(request):
	edicion=False
	desparasitante=ControlDesparasitacion.objects.all()

	if request.method=='POST':
		form=ControlDesparasitacionForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				form=ControlDesparasitacionForm()
				return HttpResponseRedirect(reverse('controlDesp:index_desp'))
			except:
				pass
		else:
			form=ControlDesparasitacionForm()

	return render(request, 'controlDesp/index_desp.html',{'vardesparasitante':desparasitante, 'edicion':edicion})

def registrar_desp(request):
	if request.method == 'POST':
		form=ControlDesparasitacionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('controlDesp:index_desp')
	else:
		form=ControlDesparasitacionForm()
	return render(request,'controlDesp/registrar_desp.html',{'form':form})

def editar_desp(request, num):
	desp=ControlDesparasitacion.objects.get(id=num)
	if request.method=='GET':
		form=ControlDesparasitacionForm(instance=desp)
	else:
		form=ControlDesparasitacionForm(request.POST, instance=desp)
		if form.is_valid():
			form.save()
			return redirect('controlDesp:index_desp')
	return render(request,'controlDesp/registrar_desp.html', {'form':form})

def eliminar_desp(request, num):  
    desp = ControlDesparasitacion.objects.get(id=num) 
    if request.method=='POST':
    	desp.delete()  
    	return redirect('controlDesp:index_desp')
    return render(request,'controlDesp/eliminar_desp.html',{'desparasitante':desp})

def nuevo_desp(request):
	if request.method=='POST':
		form=DespForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('controlDesp:index_desp')
	else:
		form=DespForm()
	return render(request, 'controlDesp/nuevo_desp.html', {'form':form})
    
