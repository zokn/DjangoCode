from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import Formulario
# Create your views here.

def busqueda_productos(request):

    return render(request, "Busqueda_productos.html")

def buscar(request):
    #CONDICIONAL PARA SABER SI EN EL TEXT SE HA INTRODUCIDO ALGO
    if request.GET["prd"]:
        #mensaje="Articulos buscado: %s" %request.GET["prd"]
        producto=request.GET["prd"]

        #if para poner un limite de texto de busqueda
        if len(producto)>20:
            mensaje="Texto demasiado largo"
            #FILTRO PARA BUSAR EN BBDD
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "Resultados_busqueda.html", {"Articulos":articulos, "query":producto})
        


    else:
        mensaje="No haz introducido nada"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method=="POST":
        miFormulario=Formulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            send_mail(infForm(['asunto'], infForm['mensaje'], 
            infForm.get('email',''),['isaac16romero2000@gmail.com'],))

            return render(request, "Gracias.html")
    
    else:

        miFormulario=Formulario()

    return render(request, "formulario_contacto.html", {"form":miFormulario})



