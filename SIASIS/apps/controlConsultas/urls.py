from django.urls import path,re_path
from apps.controlConsultas.views import CrearConsulta, listar_consultas,listar_consultasT,consultaCrear2,listar_consultasd

app_name = "controlConsultas"


urlpatterns = [
    #path('nueva', CrearConsulta.as_view(template_name = "controlConsulta/crearConsulta.html"), name = "registrar"),
	path('listar/<int:x>', listar_consultas, name="listar_consultas"),
	path('listardetalle/<int:x>', listar_consultasd, name="listar_consultasd"),
    path('listarT/', listar_consultasT, name="listar_consultasT"),
    path('nueva/<int:x>', consultaCrear2,name = "consultaCrear2"),

    


    ]
