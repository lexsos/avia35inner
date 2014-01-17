from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from .views import (
    TicketListView,
    TicketDetailView,
    AddCommentView,
    CommentsView,
)


urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name='support/support_index.html'),
        name='support_index',
    ),
    url(
        r'^my_tickets$',
        TicketListView.as_view(),
        name='support_ticket_list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        TicketDetailView.as_view(),
        name='support_ticket_detail',
    ),
    url(
        r'^ajax/comment_add/(?P<pk>\d+)/$',
        AddCommentView.as_view(),
        name='support_comment_add',
    ),
    url(
        r'^ajax/comments/(?P<pk>\d+)/$',
        CommentsView.as_view(),
        name='support_comments_get',
    ),
)
