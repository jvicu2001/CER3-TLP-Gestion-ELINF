from django.shortcuts import render
from rest_framework import generics

from .serializers import EventoSerializer

from .models import evento  

# Create your views here.
class EventoList(generics.ListAPIView):
    serializer_class = EventoSerializer
    
    def get_queryset(self):
        queryset = evento.objects.all()

        segmento = self.request.query_params.get('segmento', None)
        if segmento is not None:
            queryset = queryset.filter(segmento__nombre=segmento)
        
        tipo = self.request.query_params.get('tipo', None)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)

        return queryset