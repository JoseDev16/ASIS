from django.urls import path, re_path
from apps.controlCelo import views
from django.contrib.auth.decorators import login_required

app_name = "controlCelo"

urlpatterns = [
	path('<int:x>', (views.index_celo), name="control-celo"),
    path('index-celo/<int:x>', (views.index_celo),name="index-celo"),	
    path('registrar-vacuna-celo/<int:x>',(views.registrar_vacuna),name="registrar-vacuna-celo"),
    path('editar-celo/<int:x>/<int:num>', (views.editar_celo), name="editar-celo"),
    path('eliminar-celo/<int:x>/<int:num>', (views.eliminar_celo), name="eliminar-celo"),
]