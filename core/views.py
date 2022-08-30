
from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos

def agendamento(request):
 return render(request, 'agendamento.html')

def cadastro(request):
 return render(request, 'cadastro.html')

def base(request):
 return render(request, 'base.html')

def cabecalho(request):
 return render(request, 'cabecalho.html')

def contato(request):
 return render(request, 'contato.html')

def index(request):
 return render(request, 'index.html')

def politica_de_privacidade(request):
 return render(request, 'politica_de_privacidade.html')

def rodape(request):
 return render(request, 'rodape.html')

def login(request):
 return render(request, 'login.html')

def termos_e_servicos(request):
 return render(request, 'termos_e_servicos.html')

def listar_produtos(request):
    produto = Produtos.objects.all()
    contexto ={
        'todos_produtos': produto
    }
    return render(request, 'Produtos.html', contexto ) 
    

# Create your views here.