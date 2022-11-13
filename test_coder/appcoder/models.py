from django.db import models

# Create your models here.


class Modelos (models.Model):

    modelo = models.CharField (max_length=50)
    procedencia = models.CharField (max_length=50)
    patente = models.IntegerField ()

class Marcas (models.Model):

    modelo = models.CharField (max_length=50)
    procedencia = models.CharField (max_length=50)
    patente = models.IntegerField ()

class Peticiones_vent (models.Model):

    nombre = models.CharField (max_length=50)
    modelo = models.CharField (max_length=50)
    Fecha_de_venta = models.DateField ()



class Seccion_ingreso (models.Model):

    nombre = models.CharField (max_length=50)
    pabellon = models.IntegerField ()