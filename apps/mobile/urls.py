from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .views import MobileView, ConsumptionView


urlpatterns = patterns('',
    url(
        r'^$',
        MobileView.as_view(),
        name='mobile_index',
    ),
    url(
        r'^ajax/consumption/(?P<month>\d+)/$',
        ConsumptionView.as_view(),
        name='mobile_consumption',
    ),
)
