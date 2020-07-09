from django.urls import path, include
from rest_framework import routers
from django.contrib.admin.views.decorators import staff_member_required

from . import api
from . import views


router = routers.DefaultRouter()
router.register("carrinho", api.carrinhoViewSet)
router.register("opcionais", api.opcionaisViewSet)
router.register("cardapio", api.cardapioViewSet)
router.register("itemDoCarrinho", api.itemDoCarrinhoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("carrinho/", staff_member_required(views.carrinhoListView.as_view()), name="pedidos_carrinho_list"),
    path("carrinho/create/", views.carrinhoCreateView.as_view(), name="pedidos_carrinho_create"),
    path("carrinho/status/<int:pk>/", views.carrinhoStatusChange, name="pedidos_carrinho_status"),
    path("carrinho/detail/<int:pk>/", views.carrinhoDetailView.as_view(), name="pedidos_carrinho_detail"),
    path("carrinho/update/<int:pk>/", views.carrinhoUpdateView.as_view(), name="pedidos_carrinho_update"),
    path("carrinho/sucesso/<int:pk>/", views.carrinhoSucesso, name="pedidos_carrinho_sucesso"),
    path("opcionais/", views.opcionaisListView.as_view(), name="pedidos_opcionais_list"),
    path("opcionais/create/", views.opcionaisCreateView.as_view(), name="pedidos_opcionais_create"),
    path("opcionais/detail/<int:pk>/", views.opcionaisDetailView.as_view(), name="pedidos_opcionais_detail"),
    path("opcionais/update/<int:pk>/", views.opcionaisUpdateView.as_view(), name="pedidos_opcionais_update"),
    path("cardapio/", views.cardapioListView.as_view(), name="pedidos_cardapio_list"),
    path("cardapio/create/", views.cardapioCreateView.as_view(), name="pedidos_cardapio_create"),
    path("cardapio/detail/<int:pk>/", views.cardapioDetailView.as_view(), name="pedidos_cardapio_detail"),
    path("cardapio/update/<int:pk>/", views.cardapioUpdateView.as_view(), name="pedidos_cardapio_update"),
    path("itemDoCarrinho/", views.itemDoCarrinhoListView, name="pedidos_itemDoCarrinho_list"),
    path("itemDoCarrinho/create/", views.itemDoCarrinhoCreateView.as_view(), name="pedidos_itemDoCarrinho_create"),
    path("itemDoCarrinho/detail/<int:pk>/", views.itemDoCarrinhoDetailView.as_view(), name="pedidos_itemDoCarrinho_detail"),
    path("itemDoCarrinho/update/<int:pk>/", views.itemDoCarrinhoUpdateView.as_view(), name="pedidos_itemDoCarrinho_update"),
    path("adicionarAoCarrinho/<int:pk>/", views.adicionarAoCarrinho, name="adicionar_ao_carrinho"),
    path("itemDoCarrinho/delete/<int:pk>/", views.itemDoCarrinhoDelete, name="pedidos_itemDoCarrinho_delete"),

)
