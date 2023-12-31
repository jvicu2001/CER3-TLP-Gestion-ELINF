from typing import OrderedDict
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest.views import EventoList, SegmentoList
from rest.models import evento as eventoModel

# Create your views here.
def publicList(request: HttpRequest):
    # Obtener eventos
    eventos: OrderedDict = EventoList.as_view()(request).data
    segmentos: OrderedDict = SegmentoList.as_view()(request).data

    # Copia primeros 3 eventos
    eventos_proximos = eventos.copy()

    tipos = dict(eventoModel.tipo_choices)

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

    

        
    context = {
        'eventos': eventos,
        'segmentos': segmentos,
        'segmento_actual': int(segmento) if segmento else None,
        'tipo_actual': tipo,
        'tipos': tipos
    }

    print(request.user.is_authenticated and hasattr(request.user, 'usersegmento'))
    if request.user.is_authenticated and hasattr(request.user, 'usersegmento'):
        context['segmento_usuario'] = request.user.usersegmento.segmento.id

        # Obtener eventos proximos para el usuario actual
        eventos_proximos = [evento for evento in eventos if [
            segmento for segmento in evento['segmento'] if segmento['id'] == context['segmento_usuario']
        ]][:3]
        context['eventos_proximos'] = eventos_proximos

    return render(request, 'listadoPublico.html', context)

def segmentList(request: HttpRequest):
    return render(request, 'listadoSegmento.html')