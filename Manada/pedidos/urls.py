from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("carrinho", api.carrinhoViewSet)
router.register("opcionais", api.opcionaisViewSet)
router.register("cardapio", api.cardapioViewSet)
router.register("itemDoCarrinho", api.itemDoCarrinhoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("pedidos/carrinho/", views.carrinhoListView.as_view(), name="pedidos_carrinho_list"),
    path("pedidos/carrinho/create/", views.carrinhoCreateView.as_view(), name="pedidos_carrinho_create"),
    path("pedidos/carrinho/detail/<int:pk>/", views.carrinhoDetailView.as_view(), name="pedidos_carrinho_detail"),
    path("pedidos/carrinho/update/<int:pk>/", views.carrinhoUpdateView.as_view(), name="pedidos_carrinho_update"),
    path("pedidos/opcionais/", views.opcionaisListView.as_view(), name="pedidos_opcionais_list"),
    path("pedidos/opcionais/create/", views.opcionaisCreateView.as_view(), name="pedidos_opcionais_create"),
    path("pedidos/opcionais/detail/<int:pk>/", views.opcionaisDetailView.as_view(), name="pedidos_opcionais_detail"),
    path("pedidos/opcionais/update/<int:pk>/", views.opcionaisUpdateView.as_view(), name="pedidos_opcionais_update"),
    path("pedidos/cardapio/", views.cardapioListView.as_view(), name="pedidos_cardapio_list"),
    path("pedidos/cardapio/create/", views.cardapioCreateView.as_view(), name="pedidos_cardapio_create"),
    path("pedidos/cardapio/detail/<int:pk>/", views.cardapioDetailView.as_view(), name="pedidos_cardapio_detail"),
    path("pedidos/cardapio/update/<int:pk>/", views.cardapioUpdateView.as_view(), name="pedidos_cardapio_update"),
    path("pedidos/itemDoCarrinho/", views.itemDoCarrinhoListView.as_view(), name="pedidos_itemDoCarrinho_list"),
    path("pedidos/itemDoCarrinho/create/", views.itemDoCarrinhoCreateView.as_view(), name="pedidos_itemDoCarrinho_create"),
    path("pedidos/itemDoCarrinho/detail/<int:pk>/", views.itemDoCarrinhoDetailView.as_view(), name="pedidos_itemDoCarrinho_detail"),
    path("pedidos/itemDoCarrinho/update/<int:pk>/", views.itemDoCarrinhoUpdateView.as_view(), name="pedidos_itemDoCarrinho_update"),
    path("pedidos/adicionarAoCarrinho/<int:pk>/", views.adicionarAoCarrinho, name="adicionar_ao_carrinho"),
)
