from django.contrib import admin
from rest.models import evento, segmento

class segmento_inline(admin.TabularInline):
    model = segmento
    extra = 4

class eventoAdmin(admin.ModelAdmin):
    model = evento
    verbose_name_plural = 'Eventos'




admin.site.register(evento, eventoAdmin)
admin.site.register(segmento)
