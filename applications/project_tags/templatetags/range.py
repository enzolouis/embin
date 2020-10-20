import random

from django import template

register = template.Library()

@register.filter(name="range")
def _range(value:int):
    print("RANGE !")
    return range(int(value))

@register.filter
def randint(start:int, end:int):
	return random.randint(start, end)