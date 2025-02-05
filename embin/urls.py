"""embin URL Configuration

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
    #path('', views.home),
    # path('developers', views.developers),
    path('login', views.login_, name="login"),
    path('login/sign-in', views.sign_in, name="sign-in"),
    path('login/sign-up', views.sign_up, name="sign-up"),
    path("profile", views.profile, name="profile"),
    #path('articles/', include("applications.articles.urls")),
    path('userExists', views.userExists, name="userExists"),
      path('', include("applications.bin.urls")),
    path('admin/', admin.site.urls),

    # path('cookies/', include('cookie_consent.urls')), # django-cookie-consent extern module

    # path('accounts/', include('django.contrib.auth.urls')),
]

handler400 = "embin.views._400_error"
handler404 = "embin.views._404_page_not_found_error"

handler500 = "embin.views._500_internal_server_error"