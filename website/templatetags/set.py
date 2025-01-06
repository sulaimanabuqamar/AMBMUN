from django import template
register = template.Library()

val = None
@register.simple_tag
def set(val=None):
  return val

@register.filter
def get_item(lst, index):
    """Returns the item at the given index in a list."""
    try:
        return lst[int(index)]  # Convert index to integer
    except (IndexError, ValueError, TypeError):
        return None