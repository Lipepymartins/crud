from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
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


class ClienteUpdateView(UpdateView): #para editar clientes
    model = CLiente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_cliente")


class ClienteDetailView(DetailView):#listar clientes por id
    model = CLiente
    template_name = "lista_clienteid.html"
    context_object_name = "cliente"


class ClienteDeletView(DeleteView):#apagar clientes
    model = CLiente
    template_name = "deletado.html"
    success_url = reverse_lazy("lista_cliente")