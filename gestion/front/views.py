from django.shortcuts import render
from django.http import HttpRequest

from    rest.views import EventoList

# Create your views here.
def publicList(request: HttpRequest):
    # Obtener eventos
    eventos = EventoList.as_view()(request)

    return render(request, 'listadoPublico.html', {'eventos': eventos.data})

def segmentList(request: HttpRequest):
    return render(request, 'listadoSegmento.html')