from django import forms
from .models import Instituicao, InformacaoClienteOpenFinance, InfoClienteInstituicao
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _


class FormLogin(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput)


class CambioForm(forms.Form):
    valor_cambio = forms.CharField(
        max_length=15,
        required=True,
        label='Valor câmbio',
        label_suffix='',
    )

    valor_cambio.widget.attrs.update(
        {'placeholder': 'Insira o valor'}
    )


MOEDAS = [
    (1, 'DREX'),
    (2, 'e-CNY'),
    (3, 'Digital Euro '),
    (4, 'Digital Dollar ')
]

# class TransferenciaForm(forms.Form):
#     moeda_origem = forms.ChoiceField(
#         label="Moeda de destino",
#         choices=MOEDAS)

#     valor_trasferencia = forms.DecimalField(
#         decimal_places=2
#     )

#     saldo_drex = forms.DecimalField(
#         decimal_places=2,
#         required=True
#     )
