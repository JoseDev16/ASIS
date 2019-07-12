from django.shortcuts import render, redirect
from django.views.generic import CreateView
from apps.controlConsultas.models import Consulta
from apps.controlConsultas.forms import ConsultaForm
from apps.registroMascota.models import Expediente



# Create your views here.
class CrearConsulta(CreateView):
	model = Consulta
	templete_name = "controlConsulta/crearConsulta.html"
	form_class = ConsultaForm
	success_url = '/'

def listar_consultas(request,x):
	expediente = Expediente.objects.get(id=x)
	consulta = Consulta.objects.filter(expediente =x).order_by('id')
	contexto = {'consultas': consulta,
				'prueba':expediente }
	return render(request, 'controlConsulta/listar_consultas.html', contexto)

def listar_consultasT(request):
	consulta = Consulta.objects.all().order_by('id')
	contexto = {'consultas': consulta }
	return render(request, 'controlConsulta/listar_consultas.html', contexto)

def consultaCrear(request,x):
	expediente = Expediente.objects.get(id=x)
	form = ConsultaForm()

	if request.method == 'POST':
		form = ConsultaForm(request.POST)
		if 'btnGuardar' in request.POST:
			Consulta.expediente = expediente
			if form.is_valid():
				form.save()



		#return redirect ('controlConsultas: listar_consultas')

	context = {

		'form':form,
	}



	return render (request, 'controlConsulta/crearConsulta.html',context)


def consultaCrear2(request,x):
	form = ConsultaForm()
	expediente = Expediente.objects.get(id=x)

	if request.method=='POST':
		form=ConsultaForm(request.POST)
		if form.is_valid():
			try:
				instance = form.save(commit = False)
				instance.expediente = expediente
				instance.save()

				#return HttpResponseRedirect(reverse('controlConsulta:listar_consultas',kwargs={'x':x}))
			except:
				pass
		else:
			form=ConsultaForm()


	context ={

		'form':form,
		'prueba':expediente	


	}

	return render(request, 'controlConsulta/crearConsulta.html',context)


def listar_consultasd(request,x):
	consulta = Consulta.objects.filter(id =x)
	contexto = {'consultas': consulta }
	return render(request, 'controlConsulta/detalle.html', contexto)



