from django.shortcuts import render
from apps.registroMascota.models import Mascota
from apps.registroMascota.models import Expediente
from apps.perfilMascota.models import imagenPerfil
from apps.controlCelo.models import ControlCelo
from apps.controlConsultas.models import Consulta
from apps.controlDesp.models import ControlDesparasitacion
from apps.controlVacunas.models import ControlVacuna
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
        'id':id
    }
    if request.method == 'POST' and request.FILES['pr-pic-'+str(id)]:
        imagenPerf = request.FILES['pr-pic-'+str(id)]
        fs=FileSystemStorage()
        archivo = fs.save('pr-pic-'+str(id)+'.jpg', imagenPerf)
        url_imagen = fs.url(archivo)
        return render(request, 'perfilMascota/perfil_mascota.html', {
            'mascota':mascota,
            'celo':celo,
            'consulta':consulta,
            'desp':desparasitacion,
            'vacuna':vacuna,
            'imagenPerfil':url_imagen,
            'id':id
        })
    return render(request,'perfilMascota/perfil_mascota.html',context)
    # Create your views here.