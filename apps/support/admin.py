from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Ticket, Comment


class TicketAdmin(admin.ModelAdmin):
    list_filter = ('author', 'opened', 'create_date')
    list_display = (
        'title',
        'author',
        'create_date',
        'opened',
    )

    def make_closed(self, request, queryset):
        queryset.update(opened=False)
    make_closed.short_description = _('Mark selected %(verbose_name_plural)s as closed')

    def make_opend(self, request, queryset):
        queryset.update(opened=True)
    make_opend.short_description = _('Mark selected %(verbose_name_plural)s as opend')

    actions = (make_closed, make_opend)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('author', 'create_date')
    list_display = ('ticket', 'author', 'create_date', 'content')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
