from django.shortcuts import render
from rest_framework import generics

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import EventoSerializer, SegmentoSerializer
from .models import evento, segmento
from rest_framework.decorators import api_view

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


@api_view(['GET', 'POST', 'DELETE'])
def eventos_list (request):
    if request.method == 'GET':
        eventos = evento.objects.all()
        
        segmento = request.query_params.get('segmento', '')
        if segmento is not '':
            eventos = eventos.filter(segmento__id=segmento)
        
        tipo = request.query_params.get('tipo', '')
        if tipo is not '':
            eventos = eventos.filter(tipo=tipo)

        eventos_serializer = EventoSerializer(eventos, many=True)
        return JsonResponse(eventos_serializer.data, safe=False)
    
    elif request.method == 'POST':
        evento_data = JSONParser().parse(request)
        evento_serializer = EventoSerializer(data=evento_data)
        if evento_serializer.is_valid():
            evento_serializer.save()
            return JsonResponse(evento_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(evento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = evento.objects.all().delete()
        return JsonResponse({'message': '{} Eventos fueron eliminados exitosamente!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
def evento_detail (request, pk):
    try:
        evento = evento.objects.get(pk=pk)
    except evento.DoesNotExist:
        return JsonResponse({'message': 'El evento no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        evento_serializer = EventoSerializer(evento)
        return JsonResponse(evento_serializer.data)
    elif request.method == 'PUT':
        evento_data = JSONParser().parse(request)
        evento_serializer = EventoSerializer(evento, data=evento_data)
        if evento_serializer.is_valid():
            evento_serializer.save()
            return JsonResponse(evento_serializer.data)
        return JsonResponse(evento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        evento.delete()
        return JsonResponse({'message': 'El evento fue eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET'])
def eventos_list_published (request):
    eventos = evento.objects.filter(published=True)
        
    segmento = request.query_params.get('segmento', '')
    if segmento is not '':
        eventos = eventos.filter(segmento__id=segmento)
    
    tipo = request.query_params.get('tipo', '')
    if tipo is not '':
        eventos = eventos.filter(tipo=tipo)

    if request.method == 'GET':
        eventos_serializer = EventoSerializer(eventos, many=True)
        return JsonResponse(eventos_serializer.data, safe=False)