from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 return render(request, 'index.html')

def termos_e_servicos(request):
 return render(request, 'termos_e_servicos.html')

def politica_de_privacidade(request):
 return render(request, 'politica_de_privacidade.html')

def contato(request):
 return render(request, 'contato.html')

def agendamento(request):
 return render(request, 'agendamento.html')

def produtos(request):
 return render(request, 'produtos.html')

# Create your views here.
