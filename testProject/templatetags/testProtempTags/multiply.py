from django import template

register = template.Library()


@register.simple_tag()
def multiply(count, *args, **kwargs):
    # you would need to do any localization of the result here
    return count * 5
