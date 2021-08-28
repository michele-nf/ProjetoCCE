from django.db import models
from django.db.models.fields import CharField, EmailField


class TipoDeProfissional(models.Model):
    #Dados do tipo de profissional
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    situacao = models.BooleanField(default=False)
    updatedAt = models.DateTimeField()
    createdAt = models.DateTimeField(editable=False)


class Profissional(models.Model):
    #Dados do profissional
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    tipoDeProfissional = models.ForeignKey(TipoDeProfissional, on_delete=models.CASCADE) 
    situacao = models.BooleanField(default=False)
    updatedAt = models.DateTimeField()
    createdAt = models.DateTimeField(editable=False)