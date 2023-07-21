from django.contrib import admin
from . import models

class Filme(admin.ModelAdmin):
    list_display = ("id", "titulo", "data_lancamento", "em_cartaz")
    list_display_links = ("id", "titulo",)
    search_fields = ("titulo", "subtitulo",)
    list_filter = ("em_cartaz",)
    list_editable = ("em_cartaz", 'data_lancamento',)
    list_per_page = 10
    list_filter = ('categoria', 'usuario')

admin.site.register(models.Cartaz, Filme)


