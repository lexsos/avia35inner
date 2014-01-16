from __future__ import absolute_import
from django.template import Library

from news.models import News


register = Library()


@register.inclusion_tag('news/news_bar.html')
def news_bar():
    return {'news_list': News.objects.published()}
