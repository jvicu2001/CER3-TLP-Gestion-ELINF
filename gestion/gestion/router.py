from rest.viewsets import EventoViewSet
from rest.viewsets import SegmentoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventos', EventoViewSet)
router.register('segmentos', SegmentoViewSet)
