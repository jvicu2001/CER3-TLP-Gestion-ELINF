from rest_framework import viewsets 
from . import models
from . import serializers
from .permissions import IsAdminUserOrReadOnly


class EventoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = models.evento.objects.all()
    serializer_class = serializers.EventoSerializer
    
class SegmentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = models.segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer