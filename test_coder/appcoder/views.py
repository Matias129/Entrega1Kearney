from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render (request, "appcoder/index.html")


def modelos(request):

    return HttpResponse ("Estas en Modelos")

def marcas(request):

    return HttpResponse ("Estas en Marcas")


def peticiones_ventas(request):

    return HttpResponse ("Estas en Peticiones de ventas")


def seccion_ingreso(request):

    return HttpResponse ("Estas en Ingresos")




