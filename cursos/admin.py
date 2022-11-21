from django.contrib import admin
from . import models


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', )
    list_display_links = ('id', 'titulo', 'descricao', )


class ModuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', )
    list_display_links = ('id', 'titulo', )


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'modulo', )
    list_display_links = ('id', 'titulo', )


admin.site.register(models.Curso, CategoriaAdmin)
admin.site.register(models.Modulo, ModuloAdmin)
admin.site.register(models.Video, VideoAdmin)
