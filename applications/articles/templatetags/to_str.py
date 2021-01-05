from django import template

register = template.Library()

@register.filter(name="str")
def _str(value):
	return str(value)