from django.shortcuts import render
from django.http import HttpResponse

def agendamento(request):
 return HttpResponse(request, 'agendamento.html')

def agendamento(request):
 return render(request, 'agendamento.html')

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

def produtos(request):
 return render(request, 'produtos.html')

def rodape(request):
 return render(request, 'rodape.html')

def termos_e_servicos(request):
 return render(request, 'termos_e_servicos.html')

# Create your views here.
