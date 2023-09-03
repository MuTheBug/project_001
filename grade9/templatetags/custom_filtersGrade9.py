from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def underline(value, word):
    # print(value)
    # print(word)
    x = mark_safe(value.replace(word, '<u>' + word + '</u>'))
    # print(x)
    return x


@register.filter
def underline_and_label(value, word):

    x = mark_safe(value.replace(word.error1, '<sup>A</sup><u>' + word.error1 + '</u>',1))
    x = mark_safe(x.replace(word.error2, '<sup>B</sup><u>' + word.error2 + '</u>',1))
    x = mark_safe(x.replace(word.error3, '<sup>C</sup><u>' + word.error3 + '</u>',1))
    x = mark_safe(x.replace(word.error4, '<sup>D</sup><u>' + word.error4 + '</u>',1))

    return x
