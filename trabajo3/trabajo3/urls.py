"""trabajo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from core.views import home, cajas, Electronica, suspension
from core2.views import login, formM, guardarMarca, validarusuario, principal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',home),
    path('cajas/',cajas),
    path('Electronica/',Electronica),
    path('suspension/',suspension),
    path('login',login),
    path('formM',formM),
    path('guardarMarca/',guardarMarca),
    path('validarusuario/', validarusuario),
    path('pri/', principal),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)