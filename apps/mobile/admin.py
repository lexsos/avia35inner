from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Phone, MonthlyLimit, Month, Consumption


admin.site.register(Phone)
admin.site.register(MonthlyLimit)
admin.site.register(Month)
admin.site.register(Consumption)
