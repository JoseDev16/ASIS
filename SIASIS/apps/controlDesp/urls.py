from django.urls import path, re_path
from apps.controlDesp.views import index_desp, registrar_desp, editar_desp, eliminar_desp, nuevo_desp
from django.contrib.auth.decorators import login_required
app_name = "controlDesp"

urlpatterns = [
	path('', index_desp, name="index_desp"),
	path('index_desp/<int:x>', index_desp, name="index_desp2"),
    path('registrar_desp/', registrar_desp, name="registrar_desp"),
    path('editar_desp/<int:num>', editar_desp, name="editar_desp"),
    path('eliminar-mascota/<int:num>',eliminar_desp,name="eliminar_desp"),
    path('nuevo_desp/',nuevo_desp,name="nuevo_desp"),
]