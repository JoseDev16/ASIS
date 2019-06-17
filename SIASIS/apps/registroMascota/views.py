from django.shortcuts import render
from django.http import HttpResponse
from apps.registroMascota.forms import MascotaForm
from apps.registroMascota.models import Mascota
from django.shortcuts import redirect

# Create your views here.
def registrar_mascota(request):
    if request.method == 'POST':
    	form = MascotaForm(request.POST)
    	if form.is_valid():
    		form.save()
    	return redirect('registroMascota:listar-mascota')
    else:
    	form=MascotaForm()
    return render(request, 'registroMascota/registro_mascota.html',{'form':form})

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