from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Phone, MonthlyLimit, Month, Consumption
from .utils import make_consumptions


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'description')


class MonthlyLimitAdmin(admin.ModelAdmin):
    list_filter = ('user', 'phone')
    list_display = ('user', 'phone', 'limit_sum', 'deleted_at')


class MonthAdmin(admin.ModelAdmin):
    list_filter = ('year_number',)

    def process_month(self, request, queryset):
        for month in queryset:
            make_consumptions(request, month.pk)
    process_month.short_description = _('process selected %(verbose_name_plural)s month')

    actions = (process_month,)


class ConsumptionAdmin(admin.ModelAdmin):

    list_display = ('month', 'get_user', 'get_limit_sum', 'consumption_sum')

    def get_user(self, obj):
        return obj.monthly_limit.user
    get_user.short_description = _('user')

    def get_limit_sum(self, obj):
        return obj.monthly_limit.limit_sum
    get_limit_sum.short_description = _('limit sum')

    list_filter = ('month', 'monthly_limit__user')

admin.site.register(Phone, PhoneAdmin)
admin.site.register(MonthlyLimit, MonthlyLimitAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
