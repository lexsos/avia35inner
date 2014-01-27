import tempfile
import shutil
import os
from wand.image import Image

from django.core.files import File
from django.contrib import messages

from .settings import CONFIG
from .models import Document, Page


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


def make_pages(request, document_pk):
    document = Document.objects.get(pk=document_pk)
    clear_pages(document)

    pdf_file_name = document.document_file._get_path()
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

    messages.add_message(
        request,
        messages.INFO,
        'Make pages for "{0}"'.format(document)
    )
