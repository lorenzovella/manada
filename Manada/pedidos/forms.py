from django import forms
from . import models


class carrinhoForm(forms.ModelForm):
    class Meta:
        model = models.carrinho
        fields = ["telefone","nome","status"]


class opcionaisForm(forms.ModelForm):
    class Meta:
        model = models.opcionais
        fields = [
            "nome",
            "preco",
            "tipoDoItem",
        ]


class cardapioForm(forms.ModelForm):
    class Meta:
        model = models.cardapio
        fields = [
            "preco",
            "nome",
            "tipoDoItem",
            "descricao",
        ]


class itemDoCarrinhoForm(forms.ModelForm):
    class Meta:
        model = models.itemDoCarrinho
        fields = [
            "referenciaOpcionais",
            "referenciaCardapio",
            "referenciaCarrinho",
        ]
