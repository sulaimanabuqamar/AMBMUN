from django import template
register = template.Library()

val = None
@register.simple_tag
def set(val=None):
  return val