from django import template

register = template.Library()

@register.filter(name="first_url")
def first_url(url:str):
    return url.split("/")[1]

@register.filter
def split_url(url:str):
	return url.split("/")