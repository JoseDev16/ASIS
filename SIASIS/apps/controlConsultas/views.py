from django.shortcuts import render
from django.views.generic import CreateView
from apps.controlConsultas.models import Consulta
from apps.controlConsultas.forms import ConsultaForm


# Create your views here.
class CrearConsulta(CreateView):
	model = Consulta
	templete_name = "controlConsulta/crearConsulta.html"
	form_class = ConsultaForm
	success_url = '/'
