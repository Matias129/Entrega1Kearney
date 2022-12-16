from django.urls import path
from appcoder.views import *


urlpatterns = [
    path ("home/", home, name="home"),
    path ("modelos/", modelos, name="modelos"),
    path ("marcas/", marcas, name="marcas"),
    path ("peticiones ventas/", peticiones_ventas, name="peticiones"),
    path ("seccion ingreso/", seccion_ingreso, name="ingreso"),
    path ("prueba/", prueba, name="prueba"),
    path ("venta/crear", creacion_venta, name="crear-venta"),
]




