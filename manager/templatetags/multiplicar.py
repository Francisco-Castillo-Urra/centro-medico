from django import template
register = template.Library()
@register.simple_tag()
def multiplicacion(total, deuda):
    return round(total * deuda)