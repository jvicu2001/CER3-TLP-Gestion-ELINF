from .models import evento, segmento
from rest_framework import serializers

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'
        depth = 1

class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = segmento
        fields = '__all__'
        depth = 1