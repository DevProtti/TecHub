from django.db import models
from django.contrib.auth.models import User


# INSTITUIÇÕES FINANCEIRAS
class Instituicao(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    foto_instituicao = models.URLField()


# CARTEIRA CLIENTE
class CarteiraCliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=False, blank=False)
    agencia = models.IntegerField(null=False, blank=False)
    conta = models.IntegerField(null=False, blank=False)
    login_Instituicao = models.CharField(max_length=50, null=False, blank=False)
    senha_Instituicao = models.CharField(max_length=20, null=False, blank=False)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    saldo_drex = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)


# MOEDAS
class Moedas(models.Model):
    pass


# Items Navegação
class NavItem(models.Model):
    nome = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=100, null=True)
    icone = models.TextField(max_length=500, null=True)



