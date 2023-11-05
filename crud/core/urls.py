from django.contrib import admin
from django.urls import path, include
from .views import ClienteCreateView

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view()),
]
