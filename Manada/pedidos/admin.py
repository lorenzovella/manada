from django.contrib import admin
from django import forms

from . import models


class carrinhoAdminForm(forms.ModelForm):

    class Meta:
        model = models.carrinho
        fields = "__all__"


class carrinhoAdmin(admin.ModelAdmin):
    form = carrinhoAdminForm
    list_display = [
        "nome", 
        "telefone",
        "status",
        "created",
    ]
    readonly_fields = [
        "created",
    ]


class opcionaisAdminForm(forms.ModelForm):

    class Meta:
        model = models.opcionais
        fields = "__all__"


class opcionaisAdmin(admin.ModelAdmin):
    form = opcionaisAdminForm
    list_display = [
        "nome",
        "preco",
        "tipoDoItem",
    ]


class cardapioAdminForm(forms.ModelForm):

    class Meta:
        model = models.cardapio
        fields = "__all__"


class cardapioAdmin(admin.ModelAdmin):
    form = cardapioAdminForm
    list_display = [
        "nome",
        "preco",
        "tipoDoItem",
        "descricao",
        "imagem"
    ]


class itemDoCarrinhoAdminForm(forms.ModelForm):

    class Meta:
        model = models.itemDoCarrinho
        fields = "__all__"


class itemDoCarrinhoAdmin(admin.ModelAdmin):
    form = itemDoCarrinhoAdminForm
    list_display = [
        "referenciaCardapio",
        "referenciaCarrinho",
        "created",
    ]
    readonly_fields = [
        "created",
    ]


admin.site.register(models.carrinho, carrinhoAdmin)
admin.site.register(models.opcionais, opcionaisAdmin)
admin.site.register(models.cardapio, cardapioAdmin)
admin.site.register(models.itemDoCarrinho, itemDoCarrinhoAdmin)
