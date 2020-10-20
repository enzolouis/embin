from django.http import HttpResponse

from django.shortcuts import render

import pytz as timezone
from datetime import datetime

def home(request):

	france = datetime.now(tz=timezone.timezone("Europe/Paris")).strftime("%A, %d %B | %I:%M%p")
	england = datetime.now(tz=timezone.timezone("Europe/London")).strftime("%A, %d %B | %I:%M%p")
	germany = datetime.now(tz=timezone.timezone("Europe/Berlin")).strftime("%A, %d %B | %I:%M%p")
	spain = datetime.now(tz=timezone.timezone("Europe/Madrid")).strftime("%A, %d %B | %I:%M%p")

	timezones = [
		{"country":"France", "date":france},
		{"country":"England", "date":england},
		{"country":"Germany", "date":germany},
		{"country":"Spain", "date":spain},
	]

	return render(request, "home.html", {"timezones":timezones})


def _404_page_not_found_error(request, exception):
	try:
		return render(request, "errors/404.html", {"response":f"The url \" {exception.args[0]['path']} \" can't be reached..."})
	except:
		return render(request, "errors/404.html", {"response":exception.args[0]})


def _500_internal_server_error(request):
	return render(request, "errors/500.html")

def _400_error(request, exception):
	return HttpResponse("400")