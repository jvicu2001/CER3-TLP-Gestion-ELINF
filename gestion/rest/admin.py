from django.contrib import admin
from rest.models import evento, segmento, UserSegmento
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import segmento


class eventoAdmin(admin.ModelAdmin):
    model = evento
    verbose_name_plural = 'Eventos'

class UserSegmentoInline(admin.StackedInline):
    model = UserSegmento
    can_delete = False
    verbose_name_plural = 'Usuarios'

class UserSegmentoAdmin(BaseUserAdmin):
    inlines = (UserSegmentoInline, )

#Re-register
admin.site.unregister(User)
admin.site.register(User, UserSegmentoAdmin)

admin.site.register(evento, eventoAdmin)
admin.site.register(segmento)
