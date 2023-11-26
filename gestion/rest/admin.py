from django.contrib import admin
from rest.models import evento, segmento

class eventoAdmin(admin.ModelAdmin):
    model = evento
    verbose_name_plural = 'Eventos'


class segmentoAdmin(admin.ModelAdmin):
    model = segmento
    verbose_name_plural = 'Segmentos'

admin.site.register(evento, eventoAdmin)
