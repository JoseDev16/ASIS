from django.urls import path, re_path
from apps.controlCelo import views
from django.contrib.auth.decorators import login_required

app_name = "controlCelo"

urlpatterns = [
	path('', (views.index_celo), name="control-celo"),
    path('index-celo/', (views.index_celo),name="index-celo"),	
    path('registrar-vacuna-celo/',(views.registrar_vacuna),name="registrar-vacuna-celo"),
    path('editar-celo/<int:num>', (views.editar_celo), name="editar-celo"),
    path('eliminar-celo/<int:num>', (views.eliminar_celo), name="eliminar-celo"),
]