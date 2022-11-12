from django.http import HttpResponse
from django.template import Template, Context, loader


from datetime import datetime



def fecha_actual (request):
    hoy = datetime.now().strftime("%Y/%m/%d")

    return HttpResponse (f"Fecha actual: {hoy}")


def inicio(request):
    
    archivo = open(r"/Users/TT/Documents/AC_DJANGO/test_coder/test_coder/templates/inicio.html"   , "r")
    

    plantilla = Template (archivo.read())

    archivo.close()
#apartir de clase 18 modificamos
#creamos un diccionario con datos para la plantilla
    datos = {"nombre": "Matias", "fecha": datetime.now(), "apellido": "Kearney"}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)



def vista_listado_autos (request):
    
    archivo = open(r"C:/Users/TT/Documents/AC_DJANGO/test_coder/test_coder/templates/listado_autos.html"  , "r")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_autos = ["Ford", "Chevrolet", "Toyota", "Fiat"]

    datos = {"Mercedes_Benz": "SLS AMG", "Audi": "TT", "autoseco": listado_autos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_autos2 (request):
    
    listado_autos = ["Mitsubishi", "Honda", "Kia", "Porsche"]

    datos = {"Mercedes_Benz": "SLS AMG", "Audi": "TT", "autos_import": listado_autos}

    plantilla = loader.get_template("autos_importados.html")

    documento = plantilla.render(datos)

    return HttpResponse (documento)

