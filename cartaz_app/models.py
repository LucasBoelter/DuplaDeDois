from django.db import models

class Cartaz(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.CharField(max_length=400)
    link_trailer = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d')

    def __str__(self):
        return self.titulo
