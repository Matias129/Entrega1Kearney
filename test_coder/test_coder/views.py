from django.http import HttpResponse
from django.template import Template, Context


from datetime import datetime



def fecha_actual (request):
    hoy = datetime.now().strftime("%Y/%m/%d")

    return HttpResponse (f"Fecha actual: {hoy}")


def inicio(request):
    
    archivo = open(r"/Users/TT/Documents/AC_DJANGO/test_coder/test_coder/templates/inicio.html"   , "r")
    

    plantilla = Template (archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

