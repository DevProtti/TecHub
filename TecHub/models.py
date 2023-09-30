from django.db import models
from django.contrib.auth.models import User


# INSTITUIÇÕES FINANCEIRAS
class Instituicao(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False
    )

    foto_instituicao = models.ImageField(
        upload_to='img',
        null=True,
    )

    def __str__(self):
        return self.nome


# Info Cliente Instituição
# Agencia
# Conta
# Login
# Senha
# Usuario
# Saldo Conta
# Saldo DREX
class InfoClienteInstituicao(models.Model):  # Simula o banco de dados da instituição bancária do cliente
    Instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )


    agencia = models.CharField(
        max_length=5,
        null=False,
        blank=False
    )

    conta = models.CharField(
        null=False,
        blank=False,
        max_length=9
    )

    senha = models.CharField(
        max_length=12,
        null=False,
        blank=False
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    saldo_bancario = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True
    )

    saldo_drex = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True
    )


# CARTEIRAS CLIENTE
class InformacaoClienteOpenFinance(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='usuario'
    )

    instituicao_user = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        related_name='instituicao_user'
    )

    info_instituicao_user = models.ForeignKey(
        InfoClienteInstituicao,
        on_delete=models.CASCADE,
        related_name='info_instituicao_user'
    )

# MOEDAS
class Moedas(models.Model):
    pass


# Items Navegação
class NavItem(models.Model):
    nome = models.CharField(
        max_length=50,
        null=True
    )

    url = models.CharField(
        max_length=100,
        null=True
    )

    icone = models.TextField(
        max_length=500,
        null=True
    )

    pagina = models.CharField(
        max_length=100,
        null=True
    )
