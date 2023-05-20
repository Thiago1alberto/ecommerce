from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from . import models
# Create your views here.


class ListaProduto(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')


class AddCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('addcarrinho')


class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverCarrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
