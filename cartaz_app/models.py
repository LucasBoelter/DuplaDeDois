from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Cartaz(models.Model):
    OPCOES_CATEGORIA = [
        ('ADMINISTRADOR', 'administrador'),
        ('USUARIO', 'usuario'),
    ]
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True)
    #add categoria pra podermos selecionar qm é dps
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='administrador', null=True)
    horario1 = models.TimeField(auto_now=False, null=True)
    horario2 = models.TimeField(auto_now=False, null=True)
    data_lancamento = models.DateField(default=datetime.now)
    sinopse = models.TextField(max_length=400)
    link_trailer = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d')
    em_cartaz = models.BooleanField(default=False)
    usuario = models.ForeignKey(
        to = User,
        on_delete= models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.titulo
