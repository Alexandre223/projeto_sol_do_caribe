from dataclasses import field
from django.forms import MoelForm
form.models import Produtos
class Produtos(ModelForm):
    class Meta:
        model= Produtos
        field['nome', 'descricao','valor_compras','valor_venda']