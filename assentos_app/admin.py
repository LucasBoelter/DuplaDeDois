from django.contrib import admin
from . import models

class VendasAdmin(admin.ModelAdmin):
    list_display = ("id", "filme", "forma_pagamento","assento")
    list_display_links = ("filme",'assento')
    search_fields = ("filme", "forma_pagamento",)
    list_filter = ("filme",)
    list_editable = ()
    list_per_page = 20

admin.site.register(models.Vendas, VendasAdmin)
