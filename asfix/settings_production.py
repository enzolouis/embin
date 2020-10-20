import os
import dj_database_url

from .settings import *


DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

# https://pypi.org/project/dj-database-url/
DATABASES["default"] = dj_database_url.config()

ALLOWED_HOSTS = ["asfix.herokuapp.com"]

# http://whitenoise.evans.io/en/stable/
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


"""

Pour heroku, sur les fichier .html, il faut tout mettre en https, sinon bloquage :

" Blocage du chargement du contenu mixte actif (mixed active content) " dans le javascript

https://developer.mozilla.org/fr/docs/S%C3%A9curit%C3%A9/MixedContent/regler_probleme_contenu_mixte_site_web

"""