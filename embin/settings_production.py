import os
import dj_database_url

from .settings import *

CORS_ALLOW_ALL_ORIGINS = False # to disable in production

DEBUG = True # to disable in production
TEMPLATE_DEBUG = True # to disable in production

SECRET_KEY = os.environ["SECRET_KEY"] # in heroku

# https://pypi.org/project/dj-database-url
"""
Heroku:
DATABASES["default"] = dj_database_url.config()
"""

# Render:
database_url = os.environ["DATABASE_URL"]
DATABASES['default'] = dj_database_url.parse(database_url)


ALLOWED_HOSTS = ["embin.onrender.com", "bin.enzolouis.me"]
#CSRF_TRUSTED_ORIGINS = ['https://web-production-b040.up.railway.app']

# http://whitenoise.evans.io/en/stable/
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True
"""

"""

Pour heroku, sur les fichier .html, il faut tout mettre en https, sinon bloquage :

" Blocage du chargement du contenu mixte actif (mixed active content) " dans le javascript

https://developer.mozilla.org/fr/docs/S%C3%A9curit%C3%A9/MixedContent/regler_probleme_contenu_mixte_site_web

"""