from django import forms


class FormLogin(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput)




