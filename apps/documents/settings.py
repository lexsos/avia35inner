from django.conf import settings


CONFIG = {
    'RESOLUTION': 150,
    'COMPRESSION_QUALITY': 100,
    'INNER_PAGINATE_BY': 1,
}

CONFIG.update(getattr(settings, 'DOCUMENTS', {}))
