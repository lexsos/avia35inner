from django.conf import settings


CONFIG = {
    'PAGINATE_BY': 3,
    'BAR_LIMIT': 10,
}

CONFIG.update(getattr(settings, 'NEWS', {}))
