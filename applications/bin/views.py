from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

import json
import markdown as md

from datetime import datetime

from .paste import Paste


def paste_index(request):
    pastes = Paste.all()
    pastes.reverse()
    return render(request, "bin/paste/index.html", {'pastes':pastes})


def paste_show(request, id_):
    paste = Paste.find(id_)
    # if not find : 404 error, else :
    Paste.add_view(id_)
    return render(request, "bin/paste/show.html", {"paste":paste})



def paste_create(request):
    """
    When an user type 'http://site/bin/paste/create' (GET) :
    - Return the create page 'bin/paste/create.html'

    When an user create a paste (with form) in 'http://site/bin/paste/create' (POST) :
    - Return the redirect paste show page 'bin/paste/show.html' with their paste id : 'bin/paste/<id>'
    By creating a paste in 'bin/paste/create.html', the form :

    <form class="create" method="post" action="/bin/paste/create"> <!-- return the same page but with a django redirect (POST) -->
 
    The page form return the same page BUT not the same method, so with an only one view, ce can't do multiple page with POST/GET
    """

    if request.method == "POST":
        res = (request.POST["title"], request.POST["content"], request.POST["img"])
        print(f"{res = }")
        id_ = Paste.create_paste(*res)
        return redirect(f"./{id_}")
    else:
        return render(request, "bin/paste/create.html")


def paste_ajax_search_request(request):
    # Paste.all()
    # comparer avec request.POST["input"]
    # renvoyer HttpResponse(data, content_type="applications/json")
    # envoyer en httpresponse dans data tous les ID des posts ressemblant à la recherche
    # dans jQuerry, faire un for x of ... et document.getElementById("{x}") grâce à <div class="child" id="{{ post.id }}">
    if request.is_ajax() and request.method == "POST":
        req = request.POST["input"].lower()
        pastes = Paste.all()
        all_ = []
        for paste in pastes:
            id_ = str(paste["id"])
            title = paste["title"].lower()
            if id_ == req:
                all_.append((id_, True))
            elif req in title:
                all_.append((id_, True))
            else:
                all_.append((id_, False))


        return HttpResponse(json.dumps(all_), content_type="applications/json")
    else:
        raise Http404


# ajouter un datetime (publié le ...), une url d'image, et des tags lors de l'enregistrement en db

# mettre l'animation de la barre de chargement uniquement au moment de la recherche

# datetime.datetime.strptime("2020-10-11 00:13:08", "%Y-%m-%d %H:%M:%S")