from django.urls import path, include
from rest_framework import routers
from rest import views

router=routers.DefaultRouter()
router.register('segmento', views.SegmentoList)

urlpatterns = [
    path('', include(router.urls)),
]