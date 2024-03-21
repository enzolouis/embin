"""
WSGI config for embin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# embin.settings_production if we are in production
# embin.settings if we are not in production, in development

# os.environ.setdefault('DJANGO_SETTINGS_MODULE') => try to catch DJANGO_SETTINGS_MODULE, si il réussit,
# ca veut dire qu'il a pris la variable d'environnement sur https://dashboard.heroku.com/apps/asfix/settings donc qu'on est
# sur notre app internet avec heroku en production, donc on utilise embin.settings_production (le nom de la variable
# d'environnement heroku)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embin.settings') => si il n'a pas réussit, alors ca veut dire que l'on est
# pas sur heroku vu qu'on ne trouve pas la variable d'environnement heroku 'DJANGO_SETTINGS_MODULE', 
# on est donc en local, en développement, et non en production, et en production on utilise la configuration embin.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embin.settings')


application = get_wsgi_application()
