"""projeto_sol_do_caribe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import agendamento, base, cabecalho, cadastro, contato, index, login, politica_de_privacidade, rodape, termos_e_servicos, produtos, listar_produtos

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('admin/', admin.site.urls),
    path('', index),
    path('agendamento/', agendamento),
    path('login/', login),
    path('base/', base),
    path('cabecalho/', cabecalho),
    path('cadastro/', cadastro),
    path('politica_de_privacidade/', politica_de_privacidade),
    path('rodape/', rodape),
    path('termos_e_servicos/', termos_e_servicos),
    path('contato/', contato),
    path('rodape/', rodape),


]
