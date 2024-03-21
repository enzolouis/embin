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

def login_(request): # DON'T OVERWRITE auth.login from django
	return render(request, "login.html")

# https://docs.djangoproject.com/fr/3.1/topics/auth/default/#django.contrib.auth.authenticate

# trop bien
# https://docs.djangoproject.com/fr/3.1/ref/contrib/auth/#django.contrib.auth.get_user
def sign_in(request):
	if request.user.is_authenticated:
		return redirect("profile")

	if request.method == "GET":
		return render(request, "sign-in.html", {'form':AuthenticationForm})
	else:
		username = request.POST["username"]
		password = request.POST["password"]

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
			return redirect("/list?loginSucceed=true")
		else:
			print("--> SIGN IN : POST 4 : LOGIN ERROR")
			return render(request, "sign-in.html", {"unknown_error":True})

username_matches = string.ascii_letters + string.digits # + "_@+.-" (django default but not for my app)

def sign_up(request):
	if request.user.is_authenticated:
		return redirect("profile")

	if request.method == "GET":
		return render(request, "sign-up.html")
	else:

		username = request.POST["username"]
		password = request.POST["password"]
		password_confirm = request.POST["password_confirm"]

		for letter in username:
			if letter not in username_matches:
				return render(request, "sign-up.html", {"username_is_valid":f"\" {letter} \" is not an allowed char"})


		if len(username) > 50 or len(username) == 0:
			return render(request, "sign-up.html", {"username_is_valid":"Username is not conform (minimum 1 / maximum 50)"})
		elif len(password) > 100 or len(password) < 8:
			return render(request, "sign-up.html", {"password_is_valid":"Password is not conform (minimum 8 / maximum 100)"})

		if password_confirm != password:
			return render(request, "sign-up.html", {"password_confirm_is_valid":"Password confirm does not match"})

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			new_user = User.objects.create_user(username, password=password)
			new_user.save()
			login(request, new_user)

			return redirect("/list?registerSucceed=true")
		else:
			return render(request, "sign-up.html", {"username_is_valid":"This username already exists"})

def profile(request):
	if not request.user.is_authenticated:
		return redirect("sign-in")

	if request.method == "GET":
		return render(request, "profile.html")
	else:
		logout(request)
		return redirect("login/sign-in")


def userExists(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        username = request.POST["username"]

        if User.objects.filter(username=username).exists():
        	return HttpResponse("exist")
        else:
        	return HttpResponse("not exist")
    else:
        raise Http404

def _404_page_not_found_error(request, exception):
	try:
		return render(request, "errors/404.html", {"response":f"The url \" {exception.args[0]['path']} \" can't be reached..."})
	except:
		return render(request, "errors/404.html", {"response":exception.args[0]})


def _500_internal_server_error(request):
	return render(request, "errors/500.html")

def _400_error(request, exception):
	return HttpResponse("400")