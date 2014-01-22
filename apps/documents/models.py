import tempfile
import shutil
import os
from wand.image import Image

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.files import File

from dj_mixin.publications.models import Publication

from .settings import CONFIG


class Document(Publication):

    title = models.CharField(
        verbose_name=_('document title'),
        max_length=255,
    )
    document = models.FileField(
        upload_to='documents',
        verbose_name=_('document file'),
    )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Document, self).save(*args, **kwargs)
        make_pages(self.pk)

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


def clear_pages(document):
    for page in document.page_set.all():
        file_name = page.page_file._get_path()
        os.remove(file_name)
    document.page_set.all().delete()


def create_page(document, number, file_name):
    page_file = open(file_name, 'rb')
    django_file = File(page_file)
    page = Page(document=document, page_number=number)
    page.page_file.save(file_name, django_file)
    page.save()
    page_file.close()


def make_pages(document_pk):
    document = Document.objects.get(pk=document_pk)
    clear_pages(document)

    pdf_file_name = document.document._get_path()
    pdf_file = Image(filename=pdf_file_name, resolution=CONFIG['RESOLUTION'])
    tmp_dir = tempfile.mkdtemp()

    for page in pdf_file.sequence:
        page_number = page.index + 1
        page_img = Image(page)
        page_img.compression_quality = CONFIG['COMPRESSION_QUALITY']
        page_img_file_name = tmp_dir + \
            '/page{0}-{1}.jpg'.format(document_pk, page_number)
        page_img.save(filename=page_img_file_name)
        create_page(document, page_number, page_img_file_name)

    shutil.rmtree(tmp_dir)
