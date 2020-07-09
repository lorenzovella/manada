from django.db import models
from django.urls import reverse
from django.db.models import Sum, Count


class carrinho(models.Model):
    statusDoCarrinho = [("0","Pedido não-concluido pelo cliente"),("1","Pedido enviado ao restaurante"),("2","Pedido em preparo"),("3","Pedido concluido")]
    # Fields
    telefone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices = statusDoCarrinho, default="0")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pedidos_carrinho_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pedidos_carrinho_update", args=(self.pk,))

class opcionais(models.Model):
    tiposDoCardapio = (("Lanches","Lanches"), ("Bebidas","Bebidas"),("Porções","Porções"))
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    tipoDoItem = models.CharField(max_length=30, choices = tiposDoCardapio)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pedidos_opcionais_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pedidos_opcionais_update", args=(self.pk,))


class cardapio(models.Model):
    tiposDoCardapio = (("Lanches","Lanches"), ("Bebidas","Bebidas"),("Porções","Porções"))
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    nome = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tipoDoItem = models.CharField(max_length=30, choices = tiposDoCardapio)
    descricao = models.CharField(max_length=250)
    imagem = models.URLField(blank= True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pedidos_cardapio_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pedidos_cardapio_update", args=(self.pk,))


class itemDoCarrinho(models.Model):

    # Relationships
    referenciaOpcionais = models.ManyToManyField(opcionais, related_name='itemdocarrinho')
    referenciaCardapio = models.ForeignKey("pedidos.cardapio", on_delete=models.CASCADE, related_name = 'item')
    referenciaCarrinho = models.ForeignKey("pedidos.carrinho", on_delete=models.CASCADE, related_name='item')

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_valor_item(self):
        return self.referenciaCardapio.aggregate(Sum("preco"))['preco__sum'] + self.referenciaOpcionais.aggregate(Sum("preco"))['preco__sum']

    def get_absolute_url(self):
        return reverse("pedidos_itemDoCarrinho_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pedidos_itemDoCarrinho_update", args=(self.pk,))
