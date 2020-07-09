from django.views import generic
from . import models
from django.db.models.aggregates import Sum
from . import forms
from django.shortcuts import redirect, render, HttpResponseRedirect

def adicionarAoCarrinho(request, pk):
    if request.session.has_key('carrinho') == False:
        return redirect('pedidos_carrinho_create')
    if request.method == "POST":
        obj = request.POST;
        fooInstance = models.itemDoCarrinho()
        setattr(fooInstance,'referenciaCarrinho',models.carrinho.objects.get(pk=request.session['carrinho']));
        setattr(fooInstance,'referenciaCardapio',models.cardapio.objects.get(pk=obj['referenciaCardapio']));
        fooinstance = fooInstance.save()
        if 'referenciaOpcionais' in obj:
            for item in obj.getlist('referenciaOpcionais'):
                fooInstance.referenciaOpcionais.add(item)
        return redirect('pedidos_cardapio_list')

    item = models.cardapio.objects.get(pk=pk)
    opcionais = models.opcionais.objects.filter(tipoDoItem = item.tipoDoItem)
    context = {}
    if request.session.has_key('carrinho'):
        itensDoCarrinho = models.itemDoCarrinho.objects.filter(referenciaCarrinho=request.session['carrinho'])
        context['contador_carrinho'] = itensDoCarrinho.count()
        opt = 0
        lanches = 0
        if models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho).count() > 0:
            opt = models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho).aggregate(Sum("preco"))['preco__sum']
        if models.cardapio.objects.filter(item__in = itensDoCarrinho).count() > 0:
            lanches = models.cardapio.objects.filter(item__in = itensDoCarrinho).aggregate(Sum('preco'))['preco__sum']
        context['subtotal_carrinho'] =  lanches + opt
    else:
        context['contador_carrinho'], context['subtotal_carrinho'] = 0

    return render(request, 'pedidos/adicionar-ao-carrinho.html', {'item':item, 'opcionais':opcionais, 'context':context})



class carrinhoListView(generic.ListView):
    model = models.carrinho
    form_class = forms.carrinhoForm
    # ordering = ['-status']
    def get_queryset(self):
        return self.model.objects.exclude(status="0")



class carrinhoCreateView(generic.CreateView):
    model = models.carrinho
    form_class = forms.carrinhoForm
    def form_valid(self, form):
        instance = form.save()
        self.request.session['carrinho'] = instance.pk
        self.object = instance
        return redirect('pedidos_cardapio_list')

class carrinhoDetailView(generic.DetailView):
    model = models.carrinho
    form_class = forms.carrinhoForm


class carrinhoUpdateView(generic.UpdateView):
    model = models.carrinho
    form_class = forms.carrinhoForm
    pk_url_kwarg = "pk"

def carrinhoStatusChange(request, pk):
    instance = models.carrinho.objects.get(pk=pk)
    newStatus = min([int(instance.status) + 1,3])
    instance.status = newStatus
    instance.save()
    if(newStatus == 1):
        request.session.clear()
        return redirect('pedidos_carrinho_sucesso', pk)
    return redirect('pedidos_carrinho_list')

def carrinhoSucesso(request, pk):
    return render(request,'pedidos/carrinho_sucesso.html',{'idPedido':pk})



class opcionaisListView(generic.ListView):
    model = models.opcionais
    form_class = forms.opcionaisForm


class opcionaisCreateView(generic.CreateView):
    model = models.opcionais
    form_class = forms.opcionaisForm


class opcionaisDetailView(generic.DetailView):
    model = models.opcionais
    form_class = forms.opcionaisForm


class opcionaisUpdateView(generic.UpdateView):
    model = models.opcionais
    form_class = forms.opcionaisForm
    pk_url_kwarg = "pk"


class cardapioListView(generic.ListView):
    model = models.cardapio
    form_class = forms.cardapioForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.has_key('carrinho'):
            itensDoCarrinho = models.itemDoCarrinho.objects.filter(referenciaCarrinho=self.request.session['carrinho'])
            context['contador_carrinho'] = itensDoCarrinho.count()
            opt = 0
            lanches = 0
            if models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho).count() > 0:
                opt = models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho).aggregate(Sum("preco"))['preco__sum']
            if models.cardapio.objects.filter(item__in = itensDoCarrinho).count() > 0:
                lanches = models.cardapio.objects.filter(item__in = itensDoCarrinho).aggregate(Sum('preco'))['preco__sum']
            context['subtotal_carrinho'] =  lanches + opt
        return context

class cardapioCreateView(generic.CreateView):
    model = models.cardapio
    form_class = forms.cardapioForm


class cardapioDetailView(generic.DetailView):
    model = models.cardapio
    form_class = forms.cardapioForm


class cardapioUpdateView(generic.UpdateView):
    model = models.cardapio
    form_class = forms.cardapioForm
    pk_url_kwarg = "pk"


def itemDoCarrinhoListView(request):
        context = {}
        itensDoCarrinho = {}
        context['items'] = []
        if request.session.has_key('carrinho'):
            itensDoCarrinho = models.itemDoCarrinho.objects.filter(referenciaCarrinho=request.session['carrinho'])
            context['contador_carrinho'] = itensDoCarrinho.count()
            opt = 0
            lanches = 0
            for item in itensDoCarrinho:
                tempArr = [item, item.referenciaCardapio,item.referenciaCardapio.nome,item.referenciaCardapio.preco]
                tempArr2 = []
                for opt in item.referenciaOpcionais.all():
                    tempArr2.append([opt.nome, opt.preco])
                tempArr.append(tempArr2)
                context['items'].append(tempArr)
            if  itensDoCarrinho.count() > 0:
                lanchesQuerySet = models.cardapio.objects.filter(item__in = itensDoCarrinho)
                lanches = lanchesQuerySet.aggregate(Sum('preco'))['preco__sum']
                if models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho).count() > 0:
                    optQuerySet = models.opcionais.objects.filter(itemdocarrinho__in = itensDoCarrinho)
                    opt = optQuerySet.aggregate(Sum("preco"))['preco__sum']
            context['subtotal_carrinho'] =  lanches + opt
            return render(request, 'pedidos/itemDoCarrinho_list.html', context)

def itemDoCarrinhoDelete(request, pk):
    instance = models.itemDoCarrinho.objects.get(pk=pk)
    if(instance.referenciaCarrinho.pk == request.session['carrinho']):
        instance.delete()
    return redirect('pedidos_itemDoCarrinho_list')


class itemDoCarrinhoCreateView(generic.CreateView):
    model = models.itemDoCarrinho
    form_class = forms.itemDoCarrinhoForm


class itemDoCarrinhoDetailView(generic.DetailView):
    model = models.itemDoCarrinho
    form_class = forms.itemDoCarrinhoForm


class itemDoCarrinhoUpdateView(generic.UpdateView):
    model = models.itemDoCarrinho
    form_class = forms.itemDoCarrinhoForm
    pk_url_kwarg = "pk"
