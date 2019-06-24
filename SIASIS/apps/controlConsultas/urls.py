from django.urls import path,re_path
from apps.controlConsultas.views import CrearConsulta, listar_consultas,listar_consultasT

app_name = "controlConsultas"


urlpatterns = [
    path('nueva', CrearConsulta.as_view(template_name = "controlConsulta/crearConsulta.html"), name = "registrar"),
	path('listar/<int:x>', listar_consultas, name="listar_consultas"),
    path('listarT/', listar_consultasT, name="listar_consultasT"),

    


    ]
