from django.contrib import admin
from .models import Dialogo, Escena, Guion, HistorialCambios

# Register your models here.

@admin.register(Guion)
class GuionAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'genero', 'usuario']
    search_fields = ['titulo']


@admin.register(Escena)
class EscenaAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero_escena', 'guion']
    list_filter = ['guion']
    search_fields = ['numero_escena']
    

@admin.register(Dialogo)
class DialogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto', 'escena']
    list_filter = ['escena']
    search_fields = ['texto']


@admin.register(HistorialCambios)
class HistorialCambiosAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'guion']
    list_filter = ['guion']
    search_fields = ['guion__titulo']