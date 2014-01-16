from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class Content(Publication):
    title = models.CharField(
        verbose_name=_('content title'),
        max_length=255,
    )
    content_rich = models.TextField(
        verbose_name=_('content content rich'),
        blank=True,
    )
    content_plane = models.TextField(
        verbose_name=_('content content plane'),
        blank=True,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('content item')
        verbose_name = _('content items')
        ordering = ['-weight', '-pub_date_start']
