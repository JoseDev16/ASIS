from django.urls import path, re_path
from apps.controlCelo import views
from django.contrib.auth.decorators import login_required

app_name = "controlCelo"

urlpatterns = [
	path('control-celo/', (views.index_celo), name="control-celo"),
	
]