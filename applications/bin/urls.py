from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "bin"

urlpatterns = [
	path('', views.create, name="create"),
	path('list', views.list_, name="list"), # list à mettre avant <code> pour eviter conflit
	path('addtofav', views.add_bin_to_favorites, name="add_bin_to_favorites"),
	path('<code>', views.show, name="show"),
	path('raw/<code>', views.raw, name="show_raw"),
]
