from django.http import HttpResponse, Http404

from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home(request):
	return render(request, "home.html")

def developers(request):
	return render(request, "developers.html")

def login(request):
	return render(request, "login.html")

# https://docs.djangoproject.com/fr/3.1/topics/auth/default/#django.contrib.auth.authenticate
def sign_in(request):
	if request.method == "GET":
		return render(request, "sign-in.html")
	else:

		username = request.POST["username"]
		password = request.POST["password"]

		# john : raise
		# mityno : ok
		# ember : ok

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			username_is_valid = "Username is not valid"
			print(f"{username} DOES NOT EXIST")
		except Exception as e:
			print(f"[404] - {type(e)}")
			raise Http404("oof")
		else:
			username_is_valid = ""




		return render(request, "sign-in.html", {'username_is_valid':username_is_valid, 'password_is_valid':'Password is not valid?'})


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