from django.template import Library
from . import utils

register = Library()

# TODO: Probably not gonna use this at all
@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')

@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)

@register.filter
def cart_totals(carrinho):
    return formata_preco(utils.cart_totals(carrinho))