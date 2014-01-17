from django.views.generic import (
    ListView,
    DetailView,
)

from .models import Ticket


class TicketListView(ListView):
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        for ticket in context['ticket_list']:
            if ticket.opened and ticket.is_updated(self.request.user):
                ticket.status = 'new'
            if not ticket.opened:
                ticket.status = 'closed'
        return context


class TicketDetailView(DetailView):
    model = Ticket
