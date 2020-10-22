"""asfix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home),
    # path('developers', views.developers),
    path('login', views.login),
	path('bin/', include("applications.bin.urls")),
    path('admin/', admin.site.urls),
]

handler400 = "asfix.views._400_error"
handler404 = "asfix.views._404_page_not_found_error"

handler500 = "asfix.views._500_internal_server_error"