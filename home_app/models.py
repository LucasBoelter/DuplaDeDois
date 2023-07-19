from django.db import models

class Home(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d')

    def __str__(self):
        return self.titulo
