import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_carrinho_list_view():
    instance1 = test_helpers.create_pedidos_carrinho()
    instance2 = test_helpers.create_pedidos_carrinho()
    client = Client()
    url = reverse("pedidos_carrinho_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_carrinho_create_view():
    referenciaItem = test_helpers.create_pedidos_itemDoCarrinho()
    client = Client()
    url = reverse("pedidos_carrinho_create")
    data = {
        "telefone": "text",
        "nome": "text",
        "status": "text",
        "referenciaItem": referenciaItem.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_carrinho_detail_view():
    client = Client()
    instance = test_helpers.create_pedidos_carrinho()
    url = reverse("pedidos_carrinho_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_carrinho_update_view():
    referenciaItem = test_helpers.create_pedidos_itemDoCarrinho()
    client = Client()
    instance = test_helpers.create_pedidos_carrinho()
    url = reverse("pedidos_carrinho_update", args=[instance.pk, ])
    data = {
        "telefone": "text",
        "nome": "text",
        "status": "text",
        "referenciaItem": referenciaItem.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_opcionais_list_view():
    instance1 = test_helpers.create_pedidos_opcionais()
    instance2 = test_helpers.create_pedidos_opcionais()
    client = Client()
    url = reverse("pedidos_opcionais_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_opcionais_create_view():
    client = Client()
    url = reverse("pedidos_opcionais_create")
    data = {
        "nome": "text",
        "preco": 1,
        "tipoDoItem": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_opcionais_detail_view():
    client = Client()
    instance = test_helpers.create_pedidos_opcionais()
    url = reverse("pedidos_opcionais_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_opcionais_update_view():
    client = Client()
    instance = test_helpers.create_pedidos_opcionais()
    url = reverse("pedidos_opcionais_update", args=[instance.pk, ])
    data = {
        "nome": "text",
        "preco": 1,
        "tipoDoItem": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_cardapio_list_view():
    instance1 = test_helpers.create_pedidos_cardapio()
    instance2 = test_helpers.create_pedidos_cardapio()
    client = Client()
    url = reverse("pedidos_cardapio_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_cardapio_create_view():
    client = Client()
    url = reverse("pedidos_cardapio_create")
    data = {
        "preco": 1,
        "nome": "text",
        "tipoDoItem": "text",
        "descricao": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_cardapio_detail_view():
    client = Client()
    instance = test_helpers.create_pedidos_cardapio()
    url = reverse("pedidos_cardapio_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_cardapio_update_view():
    client = Client()
    instance = test_helpers.create_pedidos_cardapio()
    url = reverse("pedidos_cardapio_update", args=[instance.pk, ])
    data = {
        "preco": 1,
        "nome": "text",
        "tipoDoItem": "text",
        "descricao": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_itemDoCarrinho_list_view():
    instance1 = test_helpers.create_pedidos_itemDoCarrinho()
    instance2 = test_helpers.create_pedidos_itemDoCarrinho()
    client = Client()
    url = reverse("pedidos_itemDoCarrinho_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_itemDoCarrinho_create_view():
    referenciaOpcionais = test_helpers.create_pedidos_opcionais()
    referenciaCardapio = test_helpers.create_pedidos_cardapio()
    client = Client()
    url = reverse("pedidos_itemDoCarrinho_create")
    data = {
        "referenciaOpcionais": referenciaOpcionais.pk,
        "referenciaCardapio": referenciaCardapio.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_itemDoCarrinho_detail_view():
    client = Client()
    instance = test_helpers.create_pedidos_itemDoCarrinho()
    url = reverse("pedidos_itemDoCarrinho_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_itemDoCarrinho_update_view():
    referenciaOpcionais = test_helpers.create_pedidos_opcionais()
    referenciaCardapio = test_helpers.create_pedidos_cardapio()
    client = Client()
    instance = test_helpers.create_pedidos_itemDoCarrinho()
    url = reverse("pedidos_itemDoCarrinho_update", args=[instance.pk, ])
    data = {
        "referenciaOpcionais": referenciaOpcionais.pk,
        "referenciaCardapio": referenciaCardapio.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
