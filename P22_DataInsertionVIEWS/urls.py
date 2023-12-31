"""
URL configuration for P22_DataInsertionVIEWS project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_lib/', insert_lib, name='insertLib'),
    path('insert_book/', insert_Book, name='insertbook'),
    path('insert_reader/', insert_reader, name='insert_reader'),
    path('insert_reading/', insert_reading, name='insert_reading'),
    path('display_liabrary/', display_liabrary, name='display_liabrary'),
    path('display_books/', display_books, name='display_books'),
]
