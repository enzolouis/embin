## REQUIREMENTS.TXT

# DJANGO and DEPENDENCIES
- Django
- asgiref (@sync_to_async, @async_to_sync)
- pytz
- sqlparse (...)
- Jinja2 (django template (xxxxx.html))
- Werkzeug

# CDN / STATICFILES MANAGE
- whitenoise (http://whitenoise.evans.io/en/stable/) (settings_production)

# DATABASE MANAGEMENT
- psycopg2 (request)
- dj-database-url (settings_production.py)

# HEROKU UTILITES
- gunicorn


click ?
itsdangerous ?
MarkupSafe ?

# TO DO

supprimer l'applications project_tags, déplacer son dossier template_tags dans applications/bin

<style>
	* {
		color:white;
	}
	body {
		background-color:#00000f;
	}
</style>