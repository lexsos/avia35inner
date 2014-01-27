from django.db import models
from django.utils.translation import ugettext_lazy as _

from dj_mixin.publications.models import Publication


class Document(Publication):

    title = models.CharField(
        verbose_name=_('document title'),
        max_length=255,
    )
    document_file = models.FileField(
        upload_to='documents',
        verbose_name=_('document file'),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('documents items')
        verbose_name = _('document item')
        ordering = ['-weight', 'pub_date_start']


class Page(models.Model):

    document = models.ForeignKey(
        Document,
        verbose_name=_('document'),
    )
    page_file = models.FileField(
        upload_to='documents',
        verbose_name=_('page file'),
    )
    page_number = models.PositiveIntegerField(
        verbose_name=_('page number'),
    )

    def __unicode__(self):
        return unicode(self.document)

    class Meta:
        verbose_name_plural = _('pages items')
        verbose_name = _('page item')
        ordering = ('document', 'page_number')
        unique_together = ('document', 'page_number')
