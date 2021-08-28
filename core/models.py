from django.db import models
from django.db.models.fields import CharField, EmailField
from django.utils import timezone


class TipoDeProfissional(models.Model):
    #Dados do tipo de profissional
    #id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    situacao = models.BooleanField(default=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    #def salvar(self, *args, **kwargs):
        #Atualizar datas updateAt e createdAt
        #if not self.createdAt:
            #self.createdAt = timezone.now()
        #self.updatedAt = timezone.now()
        #return super(TipoDeProfissional, self).save(*args, **kwargs)


class Profissional(models.Model):
    #Dados do profissional
    #id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    tipoDeProfissional = models.ForeignKey(TipoDeProfissional, on_delete=models.CASCADE) 
    situacao = models.BooleanField(default=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    #def telefone_apenas_digitos(self):
        #Formatar telefone padrão (xx) xxxx
        #return self.telefone.replace('(', '').replace(' ', '').replace(')', '').replace('-', '')    

    #def salvar(self, *args, **kwargs):
        #Atualizar datas updateAt e createdAt
        #if not self.createdAt:
            #self.createdAt = timezone.now()
        #self.updatedAt = timezone.now()
        #return super(Profissional, self).save(*args, **kwargs)