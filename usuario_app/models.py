from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class ImagemUsuario(models.Model):
    OPCOES_CATEGORIA = [ 
        ('PESSOA', 'pessoa'),
        ('PESSOADEFICIENTE', 'pessoaDeficiente'),
    ]
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='administrador', null=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%m%d', blank=True)
    usuario = models.ForeignKey(
        to = User,
        on_delete= models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome