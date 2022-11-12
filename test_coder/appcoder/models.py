from django.db import models

# Create your models here.

class Seccion_ingreso (models.Model):

    nombre = models.CharField (max_length=50)
    pabellon = models.IntegerField ()