"""
URL configuration for diabetes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from diabetesApp.views import loginview,registerview,saveuser_view,userlogin_view,check_diabetesview,homeview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginview),
    path('login',loginview),
    path('registration/',registerview),
    path('saveuser/',saveuser_view),
    path('userlogin/',userlogin_view),
    path('check_diabetes/',check_diabetesview),
    path('home/',homeview),
]
