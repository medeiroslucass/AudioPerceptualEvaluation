from django import template

register = template.Library()
#
@register.filter
def get_referencia_id(lista):
    for element in lista:
        if element.referencia:
            return element.id
