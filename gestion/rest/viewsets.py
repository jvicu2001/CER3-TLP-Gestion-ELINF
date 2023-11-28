from rest_framework import viewsets 
from . import models
from . import serializers

class EventoViewSet(viewsets.ModelViewSet):
    queryset = models.evento.objects.all()
    serializer_class = serializers.EventoSerializer
    
class SegmentoViewSet(viewsets.ModelViewSet):
    queryset = models.segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer