from rest_framework import viewsets, permissions

from . import serializers
from . import models


class carrinhoViewSet(viewsets.ModelViewSet):
    """ViewSet for the carrinho class"""

    queryset = models.carrinho.objects.all()
    serializer_class = serializers.carrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]


class opcionaisViewSet(viewsets.ModelViewSet):
    """ViewSet for the opcionais class"""

    queryset = models.opcionais.objects.all()
    serializer_class = serializers.opcionaisSerializer
    permission_classes = [permissions.IsAuthenticated]


class cardapioViewSet(viewsets.ModelViewSet):
    """ViewSet for the cardapio class"""

    queryset = models.cardapio.objects.all()
    serializer_class = serializers.cardapioSerializer
    permission_classes = [permissions.IsAuthenticated]


class itemDoCarrinhoViewSet(viewsets.ModelViewSet):
    """ViewSet for the itemDoCarrinho class"""

    queryset = models.itemDoCarrinho.objects.all()
    serializer_class = serializers.itemDoCarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]
