from django.contrib import admin
from usuario_app.models import ImagemUsuario

class ImagemAdmin(admin.ModelAdmin):
   list_display = ('foto','usuario')
   list_display_links = ()
   search_fields = ("usuario",)
   list_filter = ('foto','usuario')
   list_editable = ('usuario',)
   list_per_page = 20

admin.site.register(ImagemUsuario, ImagemAdmin)
