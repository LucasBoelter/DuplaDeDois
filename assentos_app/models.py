from django.db import models

class Vendas(models.Model):
    OPCOES_PAGAMENTO = [
        ('DEBITO', 'debito'),
        ('CREDITO', 'credito'),
        ('PIX', 'pix'),
    ]

    filme = models.CharField(max_length=100, null=False, blank=False)
    assento = models.CharField(max_length=2, null=False, blank=False)
    forma_pagamento = models.CharField(max_length=100, choices=OPCOES_PAGAMENTO, default='')