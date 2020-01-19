from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag(takes_context=True)
def toclass(context, inputstring):
    return inputstring.strip('#')

