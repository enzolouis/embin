from django.http import HttpResponse

from django.shortcuts import render


def home(request):
	return render(request, "home.html")

def developers(request):
	return render(request, "developers.html")

def login(request):
	return render(request, "login.html")

def sign_in(request):
	return render(request, "sign-in.html")

def sign_up(request):
	return render(request, "sign-up.html")



def _404_page_not_found_error(request, exception):
	try:
		return render(request, "errors/404.html", {"response":f"The url \" {exception.args[0]['path']} \" can't be reached..."})
	except:
		return render(request, "errors/404.html", {"response":exception.args[0]})


def _500_internal_server_error(request):
	return render(request, "errors/500.html")

def _400_error(request, exception):
	return HttpResponse("400")