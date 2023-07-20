from django.contrib import admin
from django.urls import path
from . import views

app_name = "cartaz_app"

urlpatterns = [
    path('', views.view_index, name="index"),
    path('busca/', views.view_index, name="busca"),
]
