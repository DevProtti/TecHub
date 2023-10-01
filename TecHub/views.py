from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from TecHub.forms import FormLogin
from TecHub.models import NavItem, Instituicao, InfoClienteInstituicao, InformacaoClienteOpenFinance
import datetime
import locale
from .forms import CambioForm
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.contrib import messages
import requests


def cria_data_por_extenso():
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    data = datetime.date.today()
    dia_semana = datetime.datetime.strftime(data, '%A').title()
    dia = datetime.datetime.strftime(data, '%d')
    mes = datetime.datetime.strftime(data, '%B').title()
    ano = datetime.datetime.strftime(data, '%Y')
    return f'{dia_semana} {dia} de {mes} de {ano}'


def verifica_existencia_registro(id_conta_user, id_user, id_instituicao_user):
    verificacao = InformacaoClienteOpenFinance.objects.get(
        info_instituicao_user_id = id_conta_user,
        instituicao_user_id =  id_instituicao_user,
        usuario_id = id_user
        )
    if verificacao:
        return True
    return False


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


def barra_navegacao(request):
    if request.method == "GET":
        itens_navegacao = NavItem.objects.order_by('-id')
        return render(request, 'techub/barra_navegacao.html', {'itens_navegacao': itens_navegacao})


@login_required(login_url='login')
def hub_digital(request):
    if request.method == 'GET':
        instituicoes_usuario = InformacaoClienteOpenFinance.objects.all().filter(usuario=request.user)
        itens_navegacao = NavItem.objects.order_by('-id')
        data = cria_data_por_extenso()
        user_info = request.user
        url = reverse_lazy('TecHub:hub')
        context = {
            'itens': itens_navegacao,
            'user_info': user_info,
            'data': data,
            'url': url,
            'instituicoes': instituicoes_usuario
        }
        return render(request, template_name='techub/hub/hub_index.html', context=context)
    if request.method == 'POST':
        pagina = request.POST.get('name')
        success_url = reverse_lazy('TecHub:hub')
        if pagina == 'Open Finance':
            success_url = reverse_lazy('TecHub:open_finance')
        return HttpResponseRedirect(redirect_to=success_url)


@login_required(login_url='login')
def open_finance(request):
    if request.method == 'GET':
        itens_navegacao = NavItem.objects.order_by('-id')
        data = cria_data_por_extenso()
        user_info = request.user
        info_instituicoes = Instituicao.objects.all().order_by('nome')
        url = reverse_lazy('TecHub:open_finance')

        context = {
            'itens': itens_navegacao,
            'info_instituicoes': info_instituicoes,
            'user_info': user_info,
            'data': data,
            'url': url
        }
        return render(request, template_name='techub/hub/open_finance.html', context=context)
    if request.method == 'POST':
        instituicao = request.POST['instituicao']
        agencia = request.POST.get('agencia')
        conta = request.POST.get('conta')
        senha = request.POST.get('senha')
        user_id = request.user.id

        # Query da instituicao
        result_query_intituicao = Instituicao.objects.filter(id=instituicao).values('id').first()
        result_query_user_instituicao = InfoClienteInstituicao.objects.filter(Instituicao_id=instituicao).values('Instituicao_id').first()

        # Query do usuário
        result_query_user_info = InfoClienteInstituicao.objects.filter(agencia=agencia, conta=conta, senha=senha, usuario=user_id).values('id').first()
        print(result_query_user_info["id"])          
        if result_query_intituicao["id"] == result_query_user_instituicao["Instituicao_id"] and result_query_user_info != None :
                #cria um novo registro no banco de dados
                registro_user = InformacaoClienteOpenFinance(usuario=request.user, instituicao_user=Instituicao.objects.get(id=instituicao), info_instituicao_user=InfoClienteInstituicao.objects.get(id=result_query_user_info["id"]))
                registro_user.save()
                success_url = reverse_lazy('TecHub:hub')
                return HttpResponseRedirect(redirect_to=success_url)
           

def instituicao_view(request, pk):
    if request.method == 'GET':
        instituicao = InformacaoClienteOpenFinance.objects.get(pk=pk)
        user_info = request.user
        data = cria_data_por_extenso()
        itens_navegacao = NavItem.objects.order_by('-id')

        context = {
            'instituicao': instituicao,
            'user_info': user_info,
            'data': data,
            'itens': itens_navegacao
        }

        return render(request, template_name='techub/hub/instituicao_view.html', context=context)

    

def realiza_cambio(request, pk):
    instituicao = InformacaoClienteOpenFinance.objects.get(pk=pk)
    user_info = request.user
    data = cria_data_por_extenso()
    itens_navegacao = NavItem.objects.order_by('-id')
    form = CambioForm()

    context = {
            'instituicao': instituicao,
            'user_info': user_info,
            'data': data,
            'itens': itens_navegacao,
            'form': form
        }
    
    if request.method == 'GET':        
        return render(request, template_name='techub/hub/cambio.html', context=context)
    else:
        form = CambioForm(request.POST)
        if form.is_valid():
            try:
                form.cleaned_data
                chave_de_busca = InformacaoClienteOpenFinance.objects.filter(pk=pk).values('info_instituicao_user').first()['info_instituicao_user']
                info_cliente_instituicao = InfoClienteInstituicao.objects.get(pk=chave_de_busca)
                saldo_bancario = info_cliente_instituicao.saldo_bancario
                valor_cambio = form.cleaned_data['valor_cambio']
                
                if valor_cambio <= saldo_bancario:
                    novo_saldo_bancario = saldo_bancario - valor_cambio
                    novo_saldo_drex = valor_cambio  
                    info_cliente_instituicao.saldo_bancario = novo_saldo_bancario
                    info_cliente_instituicao.saldo_drex += novo_saldo_drex
                    info_cliente_instituicao.save()
                    messages.success(request, 'Câmbio realizado com sucesso')
                else:
                    raise ValidationError('O valor não pode ser maior do que seu saldo bancário')
            except ValidationError as e:
                mensagem_erro = str(e).removeprefix("['").removesuffix("']")  # Converte o erro em uma mensagem de texto
                context['erro'] = mensagem_erro
                return render(request, template_name='techub/hub/cambio.html', context=context)
            
        # Redireciona para a página com as infos da instituiçaõ do ususário
        return HttpResponseRedirect(reverse('TecHub:instituicao_view', kwargs={'pk': pk}))



def realiza_tranferencia(request, pk):
    instituicao = InformacaoClienteOpenFinance.objects.get(pk=pk)
    user_info = request.user
    data = cria_data_por_extenso()
    itens_navegacao = NavItem.objects.order_by('-id')
    moedas = [
        (1, 'DREX'),
        (2, 'e-CNY'),
        (3, 'Digital Euro '),
        (4, 'Digital Dollar ')
    ]

    context = {
        'instituicao': instituicao,
        'user_info': user_info,
        'data': data,
        'itens': itens_navegacao,
        'moedas': moedas
    }

    if request.method == 'GET':
        return render(request, template_name='techub/hub/transferencia.html', context=context)
    else:
        erros = {}
        valor_transferencia = float(request.POST.get('valor_transferencia').replace('.', '').replace(',', '.'))

        # busca as informações do saldo em DREX do cliente
        chave_de_busca = InformacaoClienteOpenFinance.objects.filter(pk=pk).values('info_instituicao_user').first()['info_instituicao_user']
        info_cliente_instituicao = InfoClienteInstituicao.objects.get(pk=chave_de_busca)
        saldo_drex = info_cliente_instituicao.saldo_drex 
       
        # Verifica se o valor da transferência é menor ou igual ao saldo em DREX:
        if valor_transferencia > saldo_drex:
            erros['valor_transferencia'] = "O valor da transferência é maior do que seu saldo DREX"
        
        if erros:
            context['erros'] = erros
            context['valor_transferencia'] = (f'{valor_transferencia:.2f}')
        else:
            # Retirando o valor transferido do saldo drex do usuario
            info_cliente_instituicao.saldo_drex -= Decimal(valor_transferencia)
            info_cliente_instituicao.save()
            messages.success(request, 'Transferência realizada com sucesso')

            # Redireciona para a página com as infos da instituiçaõ do ususário
            return HttpResponseRedirect(reverse('TecHub:instituicao_view', kwargs={'pk': pk}))
        
        return render(request, template_name='techub/hub/transferencia.html', context=context)