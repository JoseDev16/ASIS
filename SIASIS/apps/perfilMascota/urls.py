from django.urls import path, re_path
from apps.perfilMascota import views
from django.contrib.auth.decorators import login_required

app_name = "perfilMascota"

urlpatterns = [
	path('<int:id>', (views.perfil_mascota), name="perfil-mascota"),
]