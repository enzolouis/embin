import hashlib

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404

from django.contrib.auth.models import User
from .models import Bin, Tag, Favorite, Pattern
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


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
        title = request.POST["title"] or None
        author_id = request.user.id

        new_bin = Bin.objects.create(code=code, content=content, title=title, author_id=author_id) # or Bin(...).save()

        tags = request.POST["tags"] or None
        if tags:
            tags = tags.split(",")
            for tag in tags:
                tag_to_add = Tag.objects.get(name=tag)
                new_bin.tags.add(tag_to_add)

        return redirect(f"./{code}")
    else:
        tags = Tag.objects.all()
        return render(request, "bin/create.html", {"tags":tags})

def show(request, code):
    bin_ = get_bin(code)
    if bin_ is None:
        return redirect(".")

    bin_.content_line_length = len(bin_.content.splitlines())
    bin_.content = list(map(lambda x:x+"\r", bin_.content.splitlines()));

    if bin_.author_id is not None:
        bin_.author = get_user_by_id(bin_.author_id)

    return render(request, "bin/show.html", {"bin":bin_})


def raw(request, code):
    bin_ = get_bin(code)
    if bin_ is None:
        return redirect(".")

    return HttpResponse(f"<pre>{bin_.content}</pre>")

def list_(request):
    bins = Bin.objects.all().order_by('-created_at')

    for bin_ in bins:
        if bin_.author_id is not None:
            bin_.author = get_user_by_id(bin_.author_id)

    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user, bin__in=bins)
        favorite_bins_ids = set(favorite.bin_id for favorite in favorites)
        for bin_ in bins:
            bin_.is_favorite = bin_.id in favorite_bins_ids


    return render(request, "bin/list.html", {'bins':bins})


def get_user_by_id(user_id):
    try:
        user = User.objects.get(pk=user_id)
        return user
    except User.DoesNotExist:
        return None


def add_bin_to_favorites(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.user.is_authenticated:
        code = request.POST["code"]
        bin_ = get_object_or_404(Bin, code=code)
        user = request.user

        favorite = Favorite.objects.filter(bin=bin_, user=user).first()
        
        if favorite:
            favorite.delete()
            return HttpResponse("remove")
        else:
            Favorite.objects.create(bin=bin_, user=user)
            return HttpResponse("add")

    else:
        raise Http404



# Désactive CSRF pour simplifier le fetch cross-origin (à sécuriser en prod)
@csrf_exempt
def patrons(request, pk=None):
    """
    CRUD complet pour le modèle Pattern.
    GET all       -> /patrons/          (pk=None)
    GET one       -> /patrons/<id>/     (pk=<id>)
    POST add      -> /patrons/          (pk=None)
    PUT edit      -> /patrons/<id>/     (pk=<id>)
    DELETE        -> /patrons/<id>/     (pk=<id>)
    """

    # GET
    if request.method == "GET":
        if pk:
            try:
                pattern = Pattern.objects.values().get(pk=pk)
                return JsonResponse({"status": "ok", "pattern": pattern})
            except Pattern.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Pattern inconnu"}, status=404)
        else:
            patterns = Pattern.objects.all().order_by("-updated_at").values("id", "name", "created_at", "updated_at", "easeallowance", "chestCirc")
            return JsonResponse({"status": "ok", "patterns": list(patterns)})

    # POST (Add)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            pattern = Pattern.objects.create(
                name=data["name"]
            )
            return JsonResponse({"status": "ok", "id": pattern.id})
        except KeyError as e:
            return JsonResponse({"status": "error", "message": f"Champ manquant: {e}"}, status=400)

    # PUT (Edit)
    elif request.method == "PUT" and pk:
        try:
            pattern = Pattern.objects.get(pk=pk)
        except Pattern.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Pattern inconnu"}, status=404)

        try:
            data = json.loads(request.body)
            fields = [
                "name", "height", "headheight", "backwaistlength", "frontwaistlength",
                "hipdepth", "jacketlength", "dresslength", "skirtlength", "cratchlength",
                "kneelength", "trouserslength", "elbowlength", "sleevelength",
                "chestCirc", "bustcirc", "waistcirc", "hip", "neckcircumference",
                "wristcircumference", "backwidth", "backshoulderwidth", "bustheight",
                "bustdifference", "breastdistance", "easeallowance"
            ]

            for field in fields:
                if field in data:
                    setattr(pattern, field, data[field])
            pattern.save()
            return JsonResponse({"status": "ok"})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    # DELETE
    elif request.method == "DELETE" and pk:
        try:
            pattern = Pattern.objects.get(pk=pk)
            pattern.delete()
            return JsonResponse({"status": "ok"})
        except Pattern.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Pattern inconnu"}, status=404)

    else:
        return JsonResponse({"status": "error", "message": "Méthode non supportée"}, status=405)
