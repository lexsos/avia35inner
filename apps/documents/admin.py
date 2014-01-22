from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin

from .models import Document, Page


class DocumentAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('Document parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'document',)
            }
        ),
    ) + PublicationAdmin.fieldsets


class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'page_number')
    list_filter = ('document',)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Page, PageAdmin)
