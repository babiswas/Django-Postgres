from django.contrib import admin
from django.urls import path,include
from . import views

app_name='Album'

urlpatterns = [
    path('myalbum/',views.album_list,name="albums"),
]