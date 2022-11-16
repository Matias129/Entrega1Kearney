from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, "appcoder/index.html")


def modelos(request):

    return render (request, "appcoder/modelos.html")


    

def marcas(request):

    return HttpResponse ("Estas en Marcas")


def peticiones_ventas(request):

    return HttpResponse ("Estas en Peticiones de ventas")


def seccion_ingreso(request):

    return HttpResponse ("Estas en Ingresos")




