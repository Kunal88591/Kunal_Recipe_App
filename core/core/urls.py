"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

from django.contrib import admin
from django.urls import path

from Kunal_Recipe_App.views import *

from django.conf import settings
from django.conf.urls.static import static







urlpatterns = [
    path("admin/", admin.site.urls),
   
    path('receipes/', receipes ,name = "receipes") ,#siteheading , function_name , name 
    path('success/', views.success_view, name='success'),
    path('delete/<id>/', delete_receipe, name='delete'),
    path('update/<id>/', update_receipe, name='update'),
    path('register/', register, name='register'),
    path("login/", login_view, name="login"),
    path('terms/', terms, name='terms'),
    path('',my,name = "index"),
    path('contact/', contact, name='contact'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)