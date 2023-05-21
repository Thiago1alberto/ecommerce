from django.template import Library
from utils import utils

register = Library()


@register.filter
def formato_preco(val):
    return utils.formato_preco(val)
