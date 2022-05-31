from audioop import reverse
from dataclasses import fields
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PersonaForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST[ "txtAsunto"]
        mensaje = request.POST[ "txtMensaje"] + "Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["dildpizo@misena.edu.co"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")


def home(request):
    return render(request, 'index.html')

def crearPersona(request):
    if request.method == "GET":
            form = PersonaForm()
            contexto = {
                'form':form
            }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listarPersona')
    return render(request, 'crearPersona.html',contexto)


def listarPersona(request):
    persona = Persona.objects.all()
    contexto = {'persona' : persona}
    return render (request,'listarPersona.html', contexto)

def editarPersona(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        
    else:
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid():
            form.save()
        return redirect ('listarPersona')
    return render(request, 'crearPersona.html')


def eliminarPersona(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    if request.method == 'GET':
        persona.delete()
        return redirect('listarPersona')


class listadoArea(ListView):
    model = Area

class crearArea(SuccessMessageMixin, CreateView):
    model = Area
    form  = Area
    fields = '__all__'
    success_message = 'Area creada correctamente'

    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class detalleArea (DetailView):
    model = Area
 
class  editarArea(SuccessMessageMixin,UpdateView):
    model =  Area
    form = Area
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class eliminarArea(SuccessMessageMixin, DeleteView): 
    model = Area
    form = Area
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

