from django.db import models
from perfil.models import Categoria

# Create your models here.
# Onde cadastramos todas as contas mensais

class ContaPagar(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    valor = models.FloatField()
    dia_pagamento = models.IntegerField()
    
    def __str__(self):
        return self.titulo

# Aqui salva a conta paga com a data do pagamento
class ContaPaga(models.Model):
    conta = models.ForeignKey(ContaPagar, on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()