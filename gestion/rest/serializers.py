from .models import evento, segmento
from rest_framework import serializers

class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = segmento
        fields = ['id', 'nombre']
        depth = 1

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'
        depth = 1

class EventoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'