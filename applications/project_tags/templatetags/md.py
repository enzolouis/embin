from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
import markdown2 as md2

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["extra", "codehilite", "admonition"])


@register.filter()
@stringfilter
def markdown2(value):
    return md2.markdown(value)