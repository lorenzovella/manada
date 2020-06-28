from rest_framework import serializers

from . import models


class carrinhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.carrinho
        fields = [
            "telefone",
            "created",
            "last_updated",
            "nome",
            "status",
        ]

class opcionaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.opcionais
        fields = [
            "last_updated",
            "created",
            "nome",
            "preco",
            "tipoDoItem",
        ]

class cardapioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.cardapio
        fields = [
            "last_updated",
            "preco",
            "nome",
            "created",
            "tipoDoItem",
            "descricao",
        ]

class itemDoCarrinhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.itemDoCarrinho
        fields = [
            "last_updated",
            "created",
        ]
