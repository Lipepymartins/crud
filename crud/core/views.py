from django.shortcuts import render
from django.views.generic import CreateView
from .models import CLiente

# Create your views here.
class ClienteCreateView(CreateView):
    model = CLiente
    fields = "__all__"
    template_name = "form_cliente.html"