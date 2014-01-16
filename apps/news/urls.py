from django.conf.urls import patterns, url
from dj_mixin.publications.views import (
    PublicationListView,
    PublicationDetailView
)

from .models import News
from .settings import CONFIG


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(
            model=News,
            paginate_by=CONFIG['NEWS_PAGINATE_BY']
        ),
        name='news_list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        PublicationDetailView.as_view(model=News),
        name='news_detail',
    ),
)
