import hashlib

from django.shortcuts import render, redirect, HttpResponse

from .models import Bin

# numérotation ligne
# choix langages dans le create
# options imprimer dans le show
# supprimer un élément de la base de donnée si le `code` est 2 fois là. Ou alors faire une primary key

# Create your views here.

def get_bin(code):
	bin_ = Bin.objects.filter(code=code) # QuerrySet[]
	if not bin_:
		return None
	return bin_[0]

def create(request):
	if request.method == "POST":
		content = request.POST["content"]
		code = hashlib.sha256(content.encode('utf8')).hexdigest()[:6]

		Bin.objects.create(code=code, content=content) # or Bin(...).save()
		return redirect(f"./{code}")
	else:
		return render(request, "bin/create.html")

def show(request, code):
	bin_ = get_bin(code)
	if bin_ is None:
		return redirect(".")

	return render(request, "bin/show.html", {"code":bin_.code, "content":list(map(lambda x:x+"\r", bin_.content.splitlines())), "content_line_length":len(bin_.content.splitlines())})


def raw(request, code):
	bin_ = get_bin(code)
	if bin_ is None:
		return redirect(".")

	return HttpResponse(f"<pre>{bin_.content}</pre>")

def list_(request):
	return render(request, "bin/list.html")
