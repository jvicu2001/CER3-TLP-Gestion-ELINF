from django.contrib import admin
from rest.models import evento, segmento, AdminSegmento
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

class segmento_inline(admin.TabularInline):
    model = segmento
    extra = 4

class eventoAdmin(admin.ModelAdmin):
    model = evento
    verbose_name_plural = 'Eventos'

class AdminSegmentoInline(admin.StackedInline):
    model = AdminSegmento
    can_delete = False
    verbose_name_plural = 'AdminSegmentos'
    
class UserAdmin(BaseUserAdmin):
    inlines = (AdminSegmentoInline, )

#Re-register userAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(evento, eventoAdmin)
admin.site.register(segmento)
