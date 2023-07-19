from django.contrib import admin
from . import models

class VersaoAdmin(admin.ModelAdmin):
    ...

admin.site.register(Cartaz, VersaoAdmin)

