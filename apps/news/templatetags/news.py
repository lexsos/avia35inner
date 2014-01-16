from __future__ import absolute_import
from django.template import Library

from news.models import News
from news.settings import CONFIG


register = Library()


@register.inclusion_tag('news/news_bar.html')
def news_bar():
    limit = CONFIG['BAR_LIMIT']
    return {
        'news_list': News.objects.published()[:limit]
    }
