from django.conf import settings


CONFIG = {
    'PAGINATE_BY': 10,
}

CONFIG.update(getattr(settings, 'SUPPORT', {}))
