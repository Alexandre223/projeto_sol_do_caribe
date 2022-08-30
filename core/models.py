from django.db import models

class Produtos(models.Model):
    nome = models.CharField('nome', max_length=50)
    descricao = models.CharField('descricao', max_length=50)
    valor_compras = models.FloaFied('valor_compras')
    valor_venda = models.FloaFied('valor_venda')

