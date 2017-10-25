from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def str_array(str):
    res = (str.encode("utf-8")).split(',')

    return res
