from django.urls import path,re_path
from apps.controlConsultas.views import CrearConsulta, listar_consultas

app_name = "controlConsultas"


urlpatterns = [
    path('nueva', CrearConsulta.as_view(template_name = "controlConsulta/crearConsulta.html"), name = "registrar"),
	path('listar/<int:x>', listar_consultas, name="listar_consultas"),

    


    ]
