from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class ImagemUsuario(models.Model):
    OPCOES_CATEGORIA = [ 
       ('PESSOA', 'pessoa'),
        ('PESSOADEFICIENTE', 'pessoaDeficiente'),
    ]
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='', null=True)
    # nome = models.CharField(max_length=100, null=False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/')
    usuario = models.ForeignKey(
        to = User,
        on_delete= models.SET_NULL,
        null=True,
        related_name='user'
    )

    def __str__(self):
        return self.usuario