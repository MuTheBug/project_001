from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def underline(value, word):
    return mark_safe(value.replace(word, '<u>' + word + '</u>'))


@register.filter
def label_errors(text, mistake):
    html = '<span>{0}</span>'.format(text)

    errors = [mistake.error1, mistake.error2, mistake.error3, mistake.error4]
    letters = ['A', 'B', 'C', 'D']

    for i, error in enumerate(errors):
        if error:
            html = html.replace(error, '<u>{0}</u>'.format(error))
            html = html.replace(error, '{0}, {1}'.format(letters[i], error))

    return html