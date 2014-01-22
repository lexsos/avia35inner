from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Page, Document
from .settings import CONFIG


class PageListView(ListView):

    model = Page
    paginate_by = CONFIG['INNER_PAGINATE_BY']

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['document'] = get_object_or_404(
            Document,
            pk=self.kwargs['pk']
        )
        return context

    def get_queryset(self):
        queryset = super(PageListView, self).get_queryset()
        queryset = queryset.filter(document=self.kwargs['pk'])
        return queryset
