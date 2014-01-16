from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import News


class NewsAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('News parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'title',
                    'preview',
                    'content',
                    'image',
                    'date_actual_end',
                )
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('preview', 'content')


admin.site.register(News, NewsAdmin)
