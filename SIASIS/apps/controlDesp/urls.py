from django.urls import path, re_path
from apps.controlDesp import views
from django.contrib.auth.decorators import login_required

app_name = "controlDesp"

urlpatterns = [
	path('control-desparasitante/', (views.index_desp), name="control-desp"),
	

]