"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
    
Class Candidato(models.Model):
       nome = models.CharField(max_lenght=200)
        rg = models.IntegerField
        cpf = models.IntegerField
        endereço = models.CharField(max_length=300)
        telefone = models.CharField(max_lenght=15)

