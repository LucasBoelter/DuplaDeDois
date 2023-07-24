from django.db import models

class Vendas(models.Model):
    OPCOES_PAGAMENTO = [
        ('DEBITO', 'Débito'),
        ('CREDITO', 'Crédito à vista'),
        ('PIX', 'Pix'),
    ]

    filme = models.CharField(max_length=100, null=False, blank=False)
    assento = models.CharField(max_length=2, null=False, blank=False)
    forma_pagamento = models.CharField(max_length=100, choices=OPCOES_PAGAMENTO, default='')

    def __str__(self):
        return self.filme + ' ' +self.assento