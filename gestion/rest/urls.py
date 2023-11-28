from django.conf.urls import url
from rest import views

urlpatterns = [
    ulr(r'^api/eventos$', views.eventos_list),
    ulr(r'^api/eventos/(?P<pk>[0-9]+)$', views.segmentos_detail),
    url(r'^api/eventos/publicados$', views.eventos_list_published),
    ]