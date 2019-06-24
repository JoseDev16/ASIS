from django.urls import path,re_path
from apps.controlConsultas.views import CrearConsulta

urlpatterns = [
    path('', CrearConsulta.as_view(template_name = "controlConsulta/crearConsulta.html"), name = "registrar"),
    


    ]
