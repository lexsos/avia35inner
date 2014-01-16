from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Content


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=Content),
        name='index_page',
    ),
)
