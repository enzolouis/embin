from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "bin" 
# namespace to do :
# {% url 'bin:index' %}
# with the name argument to `path`

urlpatterns = [
	path('paste/', views.paste_index, name="index"),
	path('paste/<int:id_>', views.paste_show, name="show"),
	path("paste/create", views.paste_create, name="create"), # method : GET when we arrive in /bin/paste/create, POST when we submit form in bin/paste/create
	path("paste/search", views.paste_ajax_search_request, name="search"),
]
