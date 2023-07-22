from django.urls import path
from . import views

app_name='assentos_app'

urlpatterns = [
    path('', views.view_index, name="index"),
    path('pagamento/', views.view_pag, name="pag"),
]
