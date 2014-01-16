from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import Content


class ContentAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    rich_fields = ('content_rich',)

    fieldsets = (
        (
            _('Content parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'title',
                    'content_rich',
                    'content_plane',
                )
            }
        ),
    ) + PublicationAdmin.fieldsets


admin.site.register(Content, ContentAdmin)
