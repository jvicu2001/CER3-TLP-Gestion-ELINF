from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def publicList(request: HttpRequest):
    return render(request, 'listadoPublico.html')

def segmentList(request: HttpRequest):
    return render(request, 'listadoSegmento.html')