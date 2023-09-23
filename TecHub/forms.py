from django import forms


class FormLogin(forms.Form):
    login = forms.CharField(max_length=30)
    # TODO Verificar como que funciona o PasswordInput
    senha = forms.PasswordInput()

