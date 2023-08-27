from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def underline(value, word):
    return mark_safe(value.replace(word, '<u>' + word + '</u>'))
