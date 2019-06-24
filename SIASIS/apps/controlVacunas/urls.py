from django.urls import path, re_path
from apps.controlVacunas.views import index_vacu, registrar_vacu, editar_vacu, eliminar_vacu, nueva_vacu,index_vacu3
from django.contrib.auth.decorators import login_required

app_name="controlVacunas"

urlpatterns = [

	path('', index_vacu3, name="index_vacu3"),
	path('index_vacuna/<int:x>', index_vacu, name="index_vacu2"),
    path('registrar_vacuna/', registrar_vacu, name="registrar_vacu"),
    path('editar_vacuna/<int:num>', editar_vacu, name="editar_vacu"),
    path('eliminar_vacuna/<int:num>',eliminar_vacu,name="eliminar_vacu"),
    path('nueva_vacu/',nueva_vacu,name="nueva_vacu"),
    #path('index_vac/', index_vacu3, name="index_vacu3"),

]
	