from django.db import models
from django.db.models.fields import CharField, EmailField


class TipoDeProfissional(models.Model):
    #Dados do tipo de profissional
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField('Descrição', max_length=50)
    situacao = models.BooleanField('Ativo', default=True)
    updatedAt = models.DateTimeField('Data e hora da última atualização', auto_now=True)
    createdAt = models.DateTimeField('Data e hora do cadastro', auto_now_add=True)

    def __str__(self):
        return self.descricao


class Profissional(models.Model):
    #Dados do profissional
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField('E-mail')
    tipoDeProfissional = models.ForeignKey(TipoDeProfissional, on_delete=models.CASCADE, verbose_name='Tipo de Profissional') 
    situacao = models.BooleanField('Ativo', default=True)
    updatedAt = models.DateTimeField('Data e hora da última atualização', auto_now=True)
    createdAt = models.DateTimeField('Data e hora do cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome 
