from django.contrib import admin

from .models import Ticket, Comment


class TicketAdmin(admin.ModelAdmin):
    list_filter = ('author', 'opened', 'create_date')
    list_display = (
        'title',
        'author',
        'create_date',
        'opened',
    )


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('author', 'create_date')
    list_display = ('ticket', 'author', 'create_date', 'content')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
