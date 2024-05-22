from django.contrib import admin
from usuario.models import  Usuario



@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'rol',]
    list_filter = ['rol', ]
    search_fields = ['nombre', 'correo']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = False