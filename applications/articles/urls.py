from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "articles"
# namespace to do :
# {% url 'articles:index' %}
# with the name argument to `path`

urlpatterns = [
	path('', views.index, name="index"),
	path("search", views.index_ajax_search_request, name="search"),
	path('<int:id_>', views.show, name="show"),
	path("create", views.create, name="create"), # method : GET when we arrive in articles/create, POST when we submit form in articles/create
]
