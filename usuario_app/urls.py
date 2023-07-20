from django.contrib import admin
from django.urls import path
from . import views

app_name = "usuario_app"

urlpatterns = [
    path('', views.view_index, name="index"),
    path('login/', views.view_login, name="login"),
    path('cadastro/', views.view_cadastro, name="cadastro"),
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', views.logout, name="logout"),
]
