from django.conf import settings


CONFIG = {
    'NEWS_PAGINATE_BY': 3
}

CONFIG.update(getattr(settings, 'JOB_CONFIG', {}))
