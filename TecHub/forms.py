from django import forms
from .models import Instituicao, InformacaoClienteOpenFinance


class FormLogin(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput)


class FormInstituicoesUser(forms.ModelForm):
    class Meta:
        model = InformacaoClienteOpenFinance
        fields = '__all__'