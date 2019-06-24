from django.shortcuts import render
from django.views.generic import CreateView
from apps.controlConsultas.models import Consulta
from apps.controlConsultas.forms import ConsultaForm
from apps.registroMascota.models import Expediente



# Create your views here.
class CrearConsulta(CreateView):
	model = Consulta
	templete_name = "controlConsulta/crearConsulta.html"
	form_class = ConsultaForm
	success_url = '/'

def listar_consultas(request,x):
	consulta = Consulta.objects.filter(expediente =x).order_by('id')
	contexto = {'consultas': consulta }
	return render(request, 'controlConsulta/listar_consultas.html', contexto)

def listar_consultasT(request):
	consulta = Consulta.objects.all().order_by('id')
	contexto = {'consultas': consulta }
	return render(request, 'controlConsulta/listar_consultas.html', contexto)
