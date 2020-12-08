from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "pastebin"

urlpatterns = [
	path('', views.create, name="create"),
	path('<code>', views.show, name="show"),
	path('raw/<code>', views.raw, name="show_raw"),
	path('list', views.list_, name="list"),
]
