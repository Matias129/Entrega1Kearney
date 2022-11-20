from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, "appcoder/index.html")


def modelos(request):

    return render (request, "appcoder/modelos.html")


def marcas(request):

    return render (request, "appcoder/marcas.html")


def peticiones_ventas(request):

    return render (request, "appcoder/peticiones_ventas.html")


def seccion_ingreso(request):

    return render (request, "appcoder/seccion_ingreso.html")




