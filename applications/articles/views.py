from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

import json
import markdown as md

from datetime import datetime

from .articles import Articles


def index(request):
    articles = Articles.all()
    articles.reverse()
    return render(request, "articles/index.html", {'articles':articles})


def show(request, id_):
    article = Articles.find(id_)
    # if not find : 404 error, else :
    Articles.add_view(id_)
    return render(request, "articles/show.html", {"article":article})



def create(request):
    """
    When an user type 'http://site/articles/create' (GET) :
    - Return the create page 'bin/paste/create.html'

    When an user create a paste (with form) in 'http://site/articles/create' (POST) :
    - Return the redirect article show page 'articles/show.html' with their paste id : 'articles/<id>'
    By creating an article in 'articles/create.html', the form :

    <form class="create" method="post" action="articles/create"> <!-- return the same page but with a django redirect (POST) -->
 
    The page form return the same page BUT not the same method, so with an only one view, ce can't do multiple page with POST/GET
    """

    if request.method == "POST":
        res = (request.POST["title"], request.POST["content"], request.POST["img"])
        id_ = Articles.create_article(*res)
        return redirect(f"./{id_}")
    else:
        return render(request, "articles/create.html")


def index_ajax_search_request(request):
    # Paste.all()
    # comparer avec request.POST["input"]
    # renvoyer HttpResponse(data, content_type="applications/json")
    # envoyer en httpresponse dans data tous les ID des posts ressemblant à la recherche
    # dans jQuerry, faire un for x of ... et document.getElementById("{x}") grâce à <div class="child" id="{{ post.id }}">
    print(request.is_ajax() and request.method == "POST")
    if request.is_ajax() and request.method == "POST":
        print("AJAX POST")
        req = request.POST["input"].lower()
        articles = Articles.all()
        print("START FOR")
        all_ = []
        for article in articles:
            id_ = str(article["id"])
            title = article["title"].lower()
            if id_ == req:
                all_.append((id_, True))
            elif req in title:
                all_.append((id_, True))
            else:
                all_.append((id_, False))
        print("END FOR")

        return HttpResponse(json.dumps(all_), content_type="applications/json")
    else:
        raise Http404


# ajouter un datetime (publié le ...), une url d'image, et des tags lors de l'enregistrement en db

# mettre l'animation de la barre de chargement uniquement au moment de la recherche

# datetime.datetime.strptime("2020-10-11 00:13:08", "%Y-%m-%d %H:%M:%S")