from django.shortcuts import render
from django.http import HttpResponse
from apps.registroMascota.forms import MascotaForm, CuentaForm, DueñoMascotaForm
from apps.registroMascota.models import Mascota, DueñoMascota, Expediente
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView

# Create your views here.


def registrar_mascota(request):
    form = MascotaForm()
    
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES or None)
        dueno = DueñoMascota.objects.latest('id')
        if form.is_valid():
            form.save()
         
            

            if 'btnGuardar' in request.POST:
                mascota1 = Mascota.objects.latest('id')
                mascota1.dueñomascota_id= dueno.id
                mascota1.save()

                form._save_m2m()
                exp = Expediente(mascota = mascota1)
                exp.save()
                
                return redirect('registroMascota:listar-mascota')

    context = {
        'form': form,
        
    }
    return render(request, 'registroMascota/registro_mascota.html', context)


def listar_mascota(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'registroMascota/listar_mascota.html', contexto)


def editar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return(redirect('registroMascota:listar-mascota'))
    return render(request, 'registroMascota/registro_mascota.html', {'form': form})


def eliminar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('registroMascota:listar-mascota')
    return render(request, 'registroMascota/eliminar_mascota.html', {'mascota': mascota})


def registrar_due(request):
    form = CuentaForm()

    if request.POST:
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroMascota:registro-full')

    context = {
        'form': form,

    }
    return render(request, 'registroMascota/due_register.html', context)


def registro_full(request):
    form = DueñoMascotaForm()
    if request.method == 'POST':
        id_cuenta = User.objects.latest('id')
        nombre = User.objects.latest('first_name')
        apellidos = User.objects.latest('last_name')

        form = DueñoMascotaForm(request.POST, request.FILES or None)

        if form.is_valid():
            instance2 = form.save(commit=False)
            instance2.user = request.user
            instance2.save()

            if 'btnGuardar' in request.POST:
                dueno = DueñoMascota.objects.latest('id')

                dueno.cuenta_id = id_cuenta.id
                dueno.nombres = id_cuenta.first_name
                dueno.apellidos = id_cuenta.last_name

                dueno.save()
                form.save_m2m()
                return redirect('registroMascota:registrar-mascota')
    context = {
        'form': form,

    }
    return render(request, 'registroMascota/registrofull.html', context)

def listar_duenos(request):
    dueno = DueñoMascota.objects.all().order_by('id')
    contexto = {'duenos': dueno}
    return render(request, 'registroMascota/listar_dueno.html', contexto)


def listar_expedientes(request):
    expediente =Expediente.objects.all()
    contexto = {'expedientes': expediente}
    return render(request, 'registroMascota/listar_expedientes.html', contexto)

def mis_mascotas(request):
    #dueno = DueñoMascota.objects.all()
    #dueno.cuenta_id = request.user.id
    #mascota = Mascota.objects.filter(dueñomascota = dueno)
    expediente = Expediente.objects.filter(cuenta = request.user)
    contexto = {'expedientes': expediente}
    return render(request, 'registroMascota/mis_mascotas.html', contexto)

