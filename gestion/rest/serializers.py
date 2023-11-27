from .models import evento
from rest_framework import serializers

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = evento
        fields = '__all__'
        depth = 1