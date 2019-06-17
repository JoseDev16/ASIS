from django.urls import path, re_path
from apps.registroMascota import views
from django.contrib.auth.decorators import login_required

app_name = "registroMascota"

urlpatterns = [	
    path('registrar-mascota/',(views.registrar_mascota),name="registrar-mascota"),
    path('listar-mascota/',(views.listar_mascota),name="listar-mascota"),
    path('editar-mascota/<int:id_mascota>',(views.editar_mascota),name="editar-mascota"),
    path('eliminar-mascota/<int:id_mascota>',(views.eliminar_mascota),name="eliminar-mascota"),
]