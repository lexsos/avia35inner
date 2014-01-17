from django.views.generic import (
    ListView,
    DetailView,
    FormView,
)
from django.db.models import Max
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from .models import Ticket
from .forms import CommentForm


class TicketSecurityMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('support_index')
        return super(TicketSecurityMixin, self).dispatch(
                request,
                *args,
                **kwargs
        )

    def get_queryset(self):
        queryset = super(TicketSecurityMixin, self).get_queryset()
        # if not admin show only own tickets
        if not self.request.user.is_superuser:
            queryset = queryset.filter(author=self.request.user)
        return queryset


class TicketLastUpdateMixin(object):

    def get_queryset(self):
        queryset = super(TicketLastUpdateMixin, self).get_queryset()
        # Latest ticket update (latest comment)
        queryset = queryset.annotate(last_update=Max('comment__create_date'))
        return queryset


class TicketNewCommentCountMixin(object):

    sql_new_count_tmpl = """SELECT COUNT(support_comment.id)
                            FROM support_comment
                            WHERE (NOT support_comment.readed)
                                AND (support_comment.ticket_id = support_ticket.id)
                                AND (support_comment.author_id != {0})"""

    def get_queryset(self):
        queryset = super(TicketNewCommentCountMixin, self).get_queryset()
        # Count of new comment for current user
        sql_new_count = self.sql_new_count_tmpl.format(self.request.user.pk)
        queryset = queryset.extra(select={'new_count': sql_new_count})
        return queryset


class TicketListView(TicketSecurityMixin,
                     TicketLastUpdateMixin,
                     TicketNewCommentCountMixin,
                     ListView):

    model = Ticket

    def get_queryset(self):
        queryset = super(TicketListView, self).get_queryset()
        queryset = queryset.order_by('-last_update')
        return queryset


class TicketDetailView(TicketSecurityMixin,
                       TicketLastUpdateMixin, DetailView):

    model = Ticket


class CommentsView(TicketSecurityMixin, DetailView):

    model = Ticket
    template_name = 'support/comment_list.html'

    def get(self, request, *args, **kwargs):
        ticket = self.get_object()
        comments = ticket.comment_set.exclude(author=request.user)
        comments.update(readed=True)
        return super(CommentsView, self).get(request, *args, **kwargs)


class AddCommentView(FormView):

    form_class = CommentForm
    template_name = 'support/comment_form.html'

    def get_context_data(self, **kwargs):
        context = super(AddCommentView, self).get_context_data(**kwargs)
        context['ticket_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('support_comment_add', kwargs=self.kwargs)

    def form_valid(self, form):
        user = self.request.user
        ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        can_save = user.is_authenticated() and \
            (user.is_superuser or (ticket.author == user and ticket.opened))
        if can_save:
            instance = form.save(commit=False)
            instance.author = self.request.user
            instance.ticket = ticket
            instance.save()
        return super(AddCommentView, self).form_valid(form)
