from django.shortcuts import render
from apps.registroMascota.models import Mascota
from apps.registroMascota.models import Expediente
from apps.controlCelo.models import ControlCelo
from apps.controlConsultas.models import Consulta
from apps.controlDesp.models import ControlDesparasitacion
from apps.controlVacunas.models import ControlVacuna

def perfil_mascota(request,id):
    expediente = Expediente.objects.get(id=id)
    mascota=expediente.mascota
    if ControlCelo.objects.filter(expediente=expediente.id).exists():
        celo = ControlCelo.objects.filter(expediente=expediente.id).latest('id')
    else:
        celo = ''
    if Consulta.objects.filter(expediente=expediente.id).exists():
        consulta = Consulta.objects.filter(expediente=expediente.id).latest('id')
    else:
        consulta = ''
    if ControlDesparasitacion.objects.filter(expediente=expediente.id).exists():
        desparasitacion = ControlDesparasitacion.objects.filter(expediente=expediente.id).latest('id')
    else:
        desparasitacion = ''
    if ControlVacuna.objects.filter(expediente=expediente.id).exists():
        vacuna = ControlVacuna.objects.filter(expediente=expediente.id).latest('id')
    else:
        vacuna = ''
    context = {
        'mascota':mascota,
        'celo':celo,
        'consulta':consulta,
        'desp':desparasitacion,
        'vacuna':vacuna,
    }
    return render(request,'perfilMascota/perfil_mascota.html',context)
    # Create your views here.