from django.contrib import admin
from rest.models import evento, segmento, UserSegmento
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest


class eventoAdmin(admin.ModelAdmin):
    model = evento
    verbose_name_plural = 'Eventos'
    

#Re-register

admin.site.register(evento, eventoAdmin)
admin.site.register(segmento)
