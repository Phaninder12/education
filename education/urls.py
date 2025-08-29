"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from educationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview),
    path('classVIII/', views.classviiiview),
    path('classIX/', views.classixview),
    path('classX/', views.classxview),
    path('contact/', views.contactview),
    path('about/', views.aboutview),
    path('Videos/', views.videosview),
    path('Photos/', views.photoview),
    path('LatestNews/', views.newsview),
    path('ParentReg/', views.Regview),
    path('adminpage/', views.adminpageview),

]
