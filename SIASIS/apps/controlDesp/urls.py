from django.urls import path, re_path
from apps.controlDesp import views
from django.contrib.auth.decorators import login_required

app_name = "controlDesp"

urlpatterns = [
	path('<int:x>', (views.index_desparasitacion), name="index_desp2"),
    path('index-desparasitacion/<int:x>', (views.index_desparasitacion),name="index-desparasitacion"),	
    path('registrar-vacuna-desparasitacion/<int:x>',(views.registrar_vacuna),name="registrar-desparasitacion"),
    path('editar-desparasitacion/<int:x>/<int:num>', (views.editar_desparasitacion), name="editar-desparasitacion"),
    path('eliminar-desparasitacion/<int:x>/<int:num>', (views.eliminar_desparasitacion), name="eliminar-desparasitacion"),
]