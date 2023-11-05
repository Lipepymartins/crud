from django.contrib import admin
from django.urls import path, include
from .views import ClienteCreateView, ClienteListView

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view()),
    path("lista_cliente", ClienteListView.as_view(),name="lista_cliente"),
]
