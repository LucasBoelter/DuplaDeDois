from django.contrib import admin
from . import models

class Filme(admin.ModelAdmin):
    list_display = ("id", "titulo", )

admin.site.register(models.Cartaz, Filme)


