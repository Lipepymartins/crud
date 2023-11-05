from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import CLiente

# Create your views here.
class ClienteCreateView(CreateView):
    model = CLiente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_cliente"


class ClienteListView(ListView): #para listas
    model = CLiente
    template_name = "lista_cliente.html"