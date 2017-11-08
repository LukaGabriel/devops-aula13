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
    
class Candidato(models.Model):
    nome = models.CharField(max_lenght=200)
    rg = models.CharField(max_lenght=9)
    cpf = models.CharField(max_lenght=12)
    endereço = models.CharField(max_length=300)
    telefone = models.CharField(max_lenght=15)
        
class Local_Prova(models.Model):
    nome_escola = models.CharField(max_lenght=200)
    endereço = models.CharField(max_length=300)
    cidade = models.CharField(max_lenght=60)
    estado = models.CharField(max_lenght=2)

