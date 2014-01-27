from django.core.paginator import Paginator, Page, InvalidPage
from django.template import Library
from django.utils.http import urlencode


register = Library()


@register.filter
def intellipages(value, arg=None):
    if isinstance(value, Paginator) and isinstance(arg, int):
        try:
            current = value.page(arg).number
        except InvalidPage:
            return []
        count = value.num_pages
    elif isinstance(value, Page):
        current = value.number
        count = value.paginator.num_pages
    else:
        return []
    pages = []
    if current <= 5:
        pages.extend(range(1, current))
    else:
        pages.extend([1, 0] + range(current-2, current))
    pages.append(current)
    if current > count - 5:
        pages.extend(range(current+1, count+1))
    else:
        pages.extend(range(current+1, current+3) + [0, count])
    return pages


@register.simple_tag
def url_get(**kwargs):
    get_paprams = dict([[name, kwargs[name]] for name in kwargs if kwargs[name]])
    get_str = urlencode(get_paprams)
    return '?{0}'.format(get_str)
