## ERREUR LORS DU DEPLOIEMENT :
- Mettre .png au lieu de .PNG n'affiche pas l'image au déploiement, même si ca marche en local

## PROCHAINEMENT
- Ajout d'un système de commentaires sous les articles via les comptes
- Page regroupant des liens et des trucs utiles comme le projet WebTools (JavascriptProject)
- Ajouter la nav camembert pour les téléphones comme sur WebTools

## REQUIREMENTS.TXT

# DJANGO and DEPENDENCIES
- Django
- asgiref (@sync_to_async, @async_to_sync) et serveur web ASGI
- pytz
- sqlparse (...)
- Jinja2 (django template (xxxxx.html))
- Werkzeug

# CDN / STATICFILES MANAGE
- whitenoise (http://whitenoise.evans.io/en/stable/) (settings_production)

# DATABASE MANAGEMENT
- psycopg2 (request)
- dj-database-url (settings_production.py)

# HEROKU UTILITIES
- gunicorn


click ?
itsdangerous ?
MarkupSafe ?

# TO DO
- refaire le get_there_is_format dans applications/bin/articles.py, le comptage de jour/mois/année est nul
- ajouter des filtres de recherches dans /articles
- ajouter du margin en bas des bin comme /bin/axbdfc, et dans /bin, car on voit mal la dernière ligne, voire même l'avant dernière
- ET aussi l'espace entre les lignes est mal réglé pour firefox. :done:


# DID
03/01/2021 : supprimer l'applications project_tags, déplacer son dossier template_tags dans applications/bin


# Important, à sauvegarder
couleur beau rouge : #e84118

<style>
	* {
		color:white;
	}
	body {
		background-color:#00000f;
	}
</style>

# COLORS

rouge :
clair : #e84118
foncé : #c23616