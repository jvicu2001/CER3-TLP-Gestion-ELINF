from rest_framework import viewsets 
from . import models
from . import serializers
from .permissions import IsAdminUserOrReadOnly


class EventoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = models.evento.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'POST']:
            return serializers.EventoEditSerializer
        return serializers.EventoSerializer
    
class SegmentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = models.segmento.objects.all()
    serializer_class = serializers.SegmentoSerializer