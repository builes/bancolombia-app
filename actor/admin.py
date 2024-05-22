from django.contrib import admin
from actor.models import Actor, Pose, Ubicacion

# Register your models here.
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero',]
    list_filter = ['genero', ]
    search_fields = ['nombre']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = False

@admin.register(Pose)
class PoseAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'actor',]
    list_filter = ['actor', ]
    search_fields = ['nombre']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = False

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['actor',  'coordenada_x', 'coordenada_y', 'coordenada_z', 'rotacion_x', 'rotacion_y', 'rotacion_z',]
    list_filter = ['actor', ]
    search_fields = ['actor']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = False