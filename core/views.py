from django.shortcuts import render
from django.http import HttpResponse

def agendamento(request):
 return render(request, 'agendamento.html')

def base(request):
 return render(request, 'base.html')

def cabecalho(request):
 return render(request, 'cadastro.html')

def cadastro(request):
 return render(request, 'cadastro.html')

def contato(request):
 return render(request, 'contato.html')

def index(request):
 return render(request, 'index.html')

def login(request):
 return render(request, 'login.html')

def politica_de_privacidade(request):
 return render(request, 'politica_de_privacidade')

def rodape(request):
 return render(request, 'rodape')

def termos_e_servicos(request):
 return render(request, 'termos_e_servicos.html')


# Create your views here.
