from django.views.generic import ListView
from django.http import Http404
from django.db.models import Sum
from django.shortcuts import get_object_or_404

from .models import (
    Month,
    MonthlyLimit,
    Consumption,
)

class MonthMixin(object):

    def get_context_data(self, **kwargs):
        context = super(MonthMixin, self).get_context_data(**kwargs)
        context['month'] = get_object_or_404(Month, pk=self.kwargs['month'])
        return context

    def get_queryset(self):
        queryset = super(MonthMixin, self).get_queryset()
        queryset = queryset.filter(month=self.kwargs['month'])
        return queryset


class MobileView(ListView):

    model = Month
    template_name = 'mobile/mobile_index.html'

    def get_context_data(self, **kwargs):
        context = super(MobileView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            limit_list = MonthlyLimit.objects.filter(
                user=self.request.user,
                deleted_at__isnull=True,
            )
            context['limit_list'] = limit_list
        return context


class ConsumptionView(MonthMixin, ListView):

    model = Consumption
    template_name = 'mobile/ajax/consumption.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404
        return super(ConsumptionView, self).dispatch(
            request,
            *args,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(ConsumptionView, self).get_context_data(**kwargs)
        total_overrun = 0
        for consumption in self.get_queryset():
            total_overrun += consumption.get_overrun()
        context['total_overrun'] = total_overrun
        return context

    def get_queryset(self):
        queryset = super(ConsumptionView, self).get_queryset()
        queryset = queryset.filter(monthly_limit__user=self.request.user)
        return queryset


class MonthEnquiryView(MonthMixin, ListView):

    model = Consumption
    template_name = 'mobile/month_enquiry.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            raise Http404
        return super(MonthEnquiryView, self).dispatch(
            request,
            *args,
            **kwargs
        )
