from django.shortcuts import render
from django.http import HttpResponse
from apps.registroMascota.forms import MascotaForm, CuentaForm,DueñoMascotaForm
from apps.registroMascota.models import Mascota, DueñoMascota
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView

# Create your views here.
def registrar_mascota(request):
    form =MascotaForm()
    form2= CuentaForm()
    if request.is_ajax():
        form2 = CuentaForm(request.POST)
        if form2.is_valid():
            form2.save
    if request.method == 'POST':
    	form = MascotaForm(request.POST)
    	if form.is_valid():
    		form.save()
    	return redirect('registroMascota:listar-mascota')
    else:
    	form=MascotaForm()
    
    context={
		'form': form,
		'form2': form2,
		}
    return render(request, 'registroMascota/registro_mascota.html',context)

def listar_mascota(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas' : mascota}
	return render(request, 'registroMascota/listar_mascota.html', contexto)

def editar_mascota(request, id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form=MascotaForm(instance=mascota)
    else:
        form=MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return(redirect('registroMascota:listar-mascota'))
    return render(request, 'registroMascota/registro_mascota.html',{'form':form})

def eliminar_mascota(request, id_mascota):
    mascota=Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('registroMascota:listar-mascota')
    return render(request, 'registroMascota/eliminar_mascota.html',{'mascota':mascota})


def registrar_due (request):
	form = CuentaForm()
	
	if request.POST:
		form = CuentaForm(request.POST)
		if form.is_valid():
			form.save()

	context={
		'form': form,
		
		}
	return render(request, 'registroMascota/due_register.html', context)

def registro_full (request):
    if request.method == 'POST':
            id_cuenta = User.objects.lastest('id')
            form = DueñoMascotaForm(request.POST,request.FILES or None)

            if form.is_valid():
                instance2 = form.save(commit = False)
                instance2.user = request.user
                instance2.save()

            if 'btnGuardar' in request.POST:
                dueno = DueñoMascota.objects.lastest('id')
                dueno.cuenta_id = id_cuenta.id
                dueno.save()
                form.save_m2m()
                return redirect('registroMascota:listar-mascota')
    context={
		'form': form,
		
		}
    return render (request,'registroMascota: listar-mascota',context)




      



