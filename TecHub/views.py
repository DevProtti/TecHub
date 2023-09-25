from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from TecHub.forms import FormLogin
from TecHub.models import NavItem


def home(request):
    if request.method == 'GET':
        return render(request, template_name='techub/index.html')


def login(request: HttpRequest):
    if request.method == 'GET':
        form = FormLogin()
        context = {
            'form': form
        }
        return render(request, 'techub/login.html', context=context)
    elif request.method == 'POST':

        login_user = request.POST.get('login')
        senha = request.POST.get('senha')
        user = authenticate(username=login_user, password=senha)
        if user:
            login_django(request, user)
            success_url = reverse_lazy('TecHub:hub')
            return HttpResponseRedirect(redirect_to=success_url)
        else:
            unsuccess_url = reverse_lazy('TecHub:login')
            return HttpResponseRedirect(redirect_to=unsuccess_url)

@login_required(login_url='login')
def hub_digital(request):
    if request.method == 'GET':
        itens_navegacao = NavItem.objects.all()
        context = {'itens_navegacao': itens_navegacao}
        return render(request, template_name='techub/hub/digital_hub.html', context=context)


def barra_navegacao(request):
    if request.method == "GET":
        itens_navegacao = NavItem.objects.all()
        return render(request, 'techub/barra_navegacao.html', {'itens_navegacao': itens_navegacao})




# def cadastro(request: HttpRequest):
#     if request.method == 'GET':
#         return render(request, 'cadastro.html')
#     else:
#         nome = request.POST.get('nome')
#         sobrenome = request.POST.get('sobrenome')
#         login = request.POST.get('login')
#         senha = request.POST.get('senha')
#         confirma_senha = request.POST.get('confirma_senha')
#
#         user = User.objects.filter(username=login).first()
#
#         if user:
#             return HttpResponse('Esse usuário já existe')
#
#         if senha != confirma_senha:
#             return HttpResponse('Senhas não conferem')
#
#         user = User.objects.create_user(
#             username=login, first_name=nome, last_name=sobrenome, password=senha
#         )
#
#         return HttpResponse('Usuario cadatrado com sucesso!')
#
#


