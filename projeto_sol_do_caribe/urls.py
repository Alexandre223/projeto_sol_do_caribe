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
<<<<<<< HEAD
from core.views import agendamento, base, cabecalho, cadastro, contato, index, login, politica_de_privacidade, rodape, termos_e_servicos
=======
from core.views import index, agendamento, contato, termos_e_servicos, politica_de_privacidade, produtos, rodape
>>>>>>> parent of f69e88a (arrumei login,cadastro e etc...)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
<<<<<<< HEAD
    path('login/', login),
    path('politica_de_privacidade/', politica_de_privacidade),
    path('rodape/', rodape),
=======
    path('produtos/', produtos),
    path('agendamento/', agendamento),
    path('contato/', contato),
>>>>>>> parent of f69e88a (arrumei login,cadastro e etc...)
    path('termos_e_servicos/', termos_e_servicos),
    path('politica_de_privacidade/', politica_de_privacidade),
    path('rodape/', rodape),


]
