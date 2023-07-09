from django.db import models
from datetime import datetime

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
    
    def total_gasto(self):
        from extrato.models import Valores
        valores = Valores.objects.filter(categoria__id = self.id).filter(data__month=datetime.now().month).filter(tipo='S')
        
        total_valor = 0
        for valor in valores:
            total_valor += valor.valor
        return total_valor  

    def  calcula_percentual_gasto_por_categoria(self):
        #valor_planejamento -----100%
        #total_gasto--------------x
        #(total_gasto * 100) / valor_planejamento  
        return int((self.total_gasto() * 100) / self.valor_planejamento)

class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CEF', 'Caixa Econônica'),
        ('SI', 'Sicoob'),
        ('BB', 'Banco do Brasil'),
        ('PG', 'PagSeguros'),
        ('BRA', 'Bradesco'),
    )

    tipo_choices = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )


    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=3, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido
 