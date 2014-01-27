from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin

from .models import Document, Page
from .utils import make_pages


class DocumentAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('Document parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'document_file',)
            }
        ),
    ) + PublicationAdmin.fieldsets

    def make_pages(self, request, queryset):
        for document in queryset:
            make_pages(request, document.pk)
    make_pages.short_description = _('make pages for selected documents')

    actions = (make_pages,)


class PageAdmin(admin.ModelAdmin):
    list_display = ('document', 'page_number')
    list_filter = ('document',)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Page, PageAdmin)
