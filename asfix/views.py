from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# https://docs.djangoproject.com/fr/3.1/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
# il va falloir utiliser ca

import string

def home(request):
	print("--> HOME")
	return render(request, "home.html")

def developers(request):
	return render(request, "developers.html")

def login_(request): # DON'T OVERWRITE auth.login from django
	return render(request, "login.html")

# https://docs.djangoproject.com/fr/3.1/topics/auth/default/#django.contrib.auth.authenticate

# trop bien
# https://docs.djangoproject.com/fr/3.1/ref/contrib/auth/#django.contrib.auth.get_user
def sign_in(request):
	print("SIGN IN")
	if request.user.is_authenticated:
		return redirect("profile")

	if request.method == "GET":
		print("SIGN IN : GET")
		return render(request, "sign-in.html", {'form':AuthenticationForm})
	else:

		username = request.POST["username"]
		password = request.POST["password"]

		print("--> SIGN IN : POST")

		# john : raise
		# mityno : ok
		# ember : ok

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			print(f"{username} DOES NOT EXIST")
			return render(request, "sign-in.html", {"username_is_valid":"Username does not exist"})
		

		print("--> SIGN IN : POST 2")

		# if no error, check if user correspond to password

		if not user.check_password(password):
			return render(request, "sign-in.html", {"password_is_valid":"Password is not valid"})
		

		print("--> SIGN IN : POST 3")

		user = authenticate(request, username=username, password=password) # se renseigner
		if user is not None:
			print("--> SIGN IN : POST 4 : LOGIN")

			login(request, user)
			return render(request, "sign-in.html", {"sign_succeed":True, "sign_succeed_username":username})
		else:
			print("--> SIGN IN : POST 4 : LOGIN ERROR")
			return render(request, "sign-in.html", {"unknown_error":True})

username_matches = string.ascii_letters + string.digits + "_@+.-"

def sign_up(request):
	if request.user.is_authenticated:
		return redirect("profile")

	if request.method == "GET":
		return render(request, "sign-up.html")
	else:

		username = request.POST["username"]
		password = request.POST["password"]
		password_confirm = request.POST["password_confirm"]

		# _ @ + . -
		for letter in username:
			if letter not in username_matches:
				return render(request, "sign-up.html", {"username_is_valid":f"\" {letter} \" is not an allowed char"})


		if len(username) > 10 or len(username) == 0:
			return render(request, "sign-up.html", {"username_is_valid":"Username is not conform (minimum 1 / maximum 150)"})
		elif len(password) > 20 or len(password) < 8:
			return render(request, "sign-up.html", {"password_is_valid":"Password is not conform (minimum 8 / maximum 150)"})

		if password_confirm != password:
			return render(request, "sign-up.html", {"password_confirm_is_valid":"Password confirm is not equals to password"})

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			new_user = User.objects.create_user(username, password=password)
			new_user.save()
			login(request, new_user)
			return render(request, "sign-up.html", {"sign_succeed":True, "sign_succeed_username":username})
		else:
			return render(request, "sign-up.html", {"username_is_valid":"This username already exists"})

def profile(request):
	if not request.user.is_authenticated:
		return redirect("sign-in")

	if request.method == "GET":
		print(dir(request.user))
		print(request.user.last_login)
		print(request.user.username)
		return render(request, "profile.html")
	else:
		logout(request)
		return redirect("login/sign-in") #redirect !

def _404_page_not_found_error(request, exception):
	try:
		return render(request, "errors/404.html", {"response":f"The url \" {exception.args[0]['path']} \" can't be reached..."})
	except:
		return render(request, "errors/404.html", {"response":exception.args[0]})


def _500_internal_server_error(request):
	return render(request, "errors/500.html")

def _400_error(request, exception):
	return HttpResponse("400")