from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_desp(request):
    return HttpResponse("Hola mundo desde desparasitante")