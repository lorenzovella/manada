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
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class opcionaisAdminForm(forms.ModelForm):

    class Meta:
        model = models.opcionais
        fields = "__all__"


class opcionaisAdmin(admin.ModelAdmin):
    form = opcionaisAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class cardapioAdminForm(forms.ModelForm):

    class Meta:
        model = models.cardapio
        fields = "__all__"


class cardapioAdmin(admin.ModelAdmin):
    form = cardapioAdminForm
    list_display = [
        "last_updated",
        "preco",
        "nome",
        "created",
        "tipoDoItem",
        "descricao",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class itemDoCarrinhoAdminForm(forms.ModelForm):

    class Meta:
        model = models.itemDoCarrinho
        fields = "__all__"


class itemDoCarrinhoAdmin(admin.ModelAdmin):
    form = itemDoCarrinhoAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.carrinho, carrinhoAdmin)
admin.site.register(models.opcionais, opcionaisAdmin)
admin.site.register(models.cardapio, cardapioAdmin)
admin.site.register(models.itemDoCarrinho, itemDoCarrinhoAdmin)
