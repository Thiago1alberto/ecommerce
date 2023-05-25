from django.template import Library
from utils import utils

register = Library()


@register.filter
def formato_preco(val):
    return utils.formato_preco(val)


@register.filter
def qtd_total_carrinho(carrinho):
    return utils.qtd_total_carrinho(carrinho)


@register.filter
def carrinho_valor_total(carrinho):
    return utils.carrinho_valor_total(carrinho)
