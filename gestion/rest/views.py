from django.shortcuts import render
from rest_framework import generics

from .serializers import EventoSerializer, SegmentoSerializer

from .models import evento, segmento

# Create your views here.
class EventoList(generics.ListAPIView):
    serializer_class = EventoSerializer
    
    def get_queryset(self):
        queryset = evento.objects.all()

        segmento = self.request.query_params.get('segmento', '')
        if segmento is not '':
            queryset = queryset.filter(segmento__id=segmento)
        
        tipo = self.request.query_params.get('tipo', '')
        if tipo is not '':
            queryset = queryset.filter(tipo=tipo)

        return queryset
    
class SegmentoList(generics.ListAPIView):
    serializer_class = SegmentoSerializer

    def get_queryset(self):
        queryset = segmento.objects.all()

        return queryset
