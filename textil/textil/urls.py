"""textil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal.views import crearArea, crearPersona, detalleArea, editarArea, editarPersona, eliminarArea, eliminarPersona, formularioContacto, contactar, home, listadoArea, listarPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),
    path('crearPersona/', crearPersona),
    path('index/', home, name="index"),
    path('listarPersona/', listarPersona, name="listarPersona"),
    path('editarPersona/<int:id_persona>/', editarPersona, name="editarPersona"),
    path('eliminarPersona/<int:id_persona>/', eliminarPersona, name="eliminarPersona"),
    


    path('area/', listadoArea.as_view(template_name="area/index1.html"), name='leer'),
     # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('area/detalle/<int:pk>', detalleArea.as_view(template_name = "area/detalle.html"), name='detalle'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('area/crear/', crearArea.as_view(template_name = "area/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('area/editar/<int:pk>', editarArea.as_view(template_name = "area/editar.html"), name='editar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('area/eliminar/<int:pk>', eliminarArea.as_view(), name="area/eliminar.html"),  
]
