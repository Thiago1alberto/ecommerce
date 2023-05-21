from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views import View
from . import models
# Create your views here.


class ListaProduto(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 6


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


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
