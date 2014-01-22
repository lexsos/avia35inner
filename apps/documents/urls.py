from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Document
from .views import PageListView


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=Document),
        name='document_list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        PageListView.as_view(),
        name='document_page_list',
    ),

)
