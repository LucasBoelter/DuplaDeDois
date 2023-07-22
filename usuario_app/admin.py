from django.contrib import admin
from usuario_app.models import ImagemUsuario

class ImagemAdmin(admin.ModelAdmin):
    list_filter = ('categoria','pessoa')

admin.site.register(ImagemUsuario, ImagemAdmin)
