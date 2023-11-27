from typing import OrderedDict
from django.shortcuts import render
from django.http import HttpRequest

from rest.views import EventoList, SegmentoList
from rest.models import evento as eventoModel

# Create your views here.
def publicList(request: HttpRequest):
    # Obtener eventos
    eventos: OrderedDict = EventoList.as_view()(request).data
    segmentos: OrderedDict = SegmentoList.as_view()(request).data

    tipos = eventoModel.tipo_choices

    # Filtrar eventos
    tipo = request.GET.get('tipo')
    segmento = request.GET.get('segmento')

    if tipo:
        eventos = list(filter(lambda x: x['tipo'] == tipo, eventos))   
    
    if segmento:
        eventos = list(filter(
            lambda eventos_a_filtrar: 
                map(lambda segmentos_evento: 
                    segmentos_evento['id'], eventos_a_filtrar['segmento']
                ), eventos
            ))

    return render(request, 'listadoPublico.html', {
        'eventos': eventos,
        'segmentos': segmentos,
        'segmento_actual': int(segmento) if segmento else None,
        'tipo_actual': tipo,
        'tipos': tipos
        })

def segmentList(request: HttpRequest):
    return render(request, 'listadoSegmento.html')