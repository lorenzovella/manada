import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from pedidos import models as pedidos_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_pedidos_carrinho(**kwargs):
    defaults = {}
    defaults["telefone"] = ""
    defaults["nome"] = ""
    defaults["status"] = ""
    if "referenciaItem" not in kwargs:
        defaults["referenciaItem"] = create_pedidos_itemDoCarrinho()
    defaults.update(**kwargs)
    return pedidos_models.carrinho.objects.create(**defaults)
def create_pedidos_opcionais(**kwargs):
    defaults = {}
    defaults["nome"] = ""
    defaults["preco"] = ""
    defaults["tipoDoItem"] = ""
    defaults.update(**kwargs)
    return pedidos_models.opcionais.objects.create(**defaults)
def create_pedidos_cardapio(**kwargs):
    defaults = {}
    defaults["preco"] = ""
    defaults["nome"] = ""
    defaults["tipoDoItem"] = ""
    defaults["descricao"] = ""
    defaults.update(**kwargs)
    return pedidos_models.cardapio.objects.create(**defaults)
def create_pedidos_itemDoCarrinho(**kwargs):
    defaults = {}
    if "referenciaOpcionais" not in kwargs:
        defaults["referenciaOpcionais"] = create_pedidos_opcionais()
    if "referenciaCardapio" not in kwargs:
        defaults["referenciaCardapio"] = create_pedidos_cardapio()
    defaults.update(**kwargs)
    return pedidos_models.itemDoCarrinho.objects.create(**defaults)
