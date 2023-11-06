from django.contrib import admin
from django.urls import path, include
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDetailView, ClienteDeletView

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view()),
    path("lista_cliente", ClienteListView.as_view(),name="lista_cliente"),
    path("form_cliente/<int:pk>", ClienteUpdateView.as_view(), name="editar_cliente"),
    path("lista_clienteid/<int:pk>", ClienteDetailView.as_view(),name="exibir_cliente"),
    path("delete_cliente/<int:pk>", ClienteDeletView.as_view(),name="deletar_cliente"),
]
