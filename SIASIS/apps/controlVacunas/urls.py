from django.urls import path, re_path
from apps.controlVacunas import views
from django.contrib.auth.decorators import login_required

app_name = "controlVacunas"

urlpatterns = [
	path('control-vacunas/', (views.index), name="control"),
	

]