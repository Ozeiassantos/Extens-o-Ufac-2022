from django.shortcuts import render
from django.views.gereric.edit import CreateView
from django.views.gereric.list import ListView
from .models import Clientes

#serve para redirecionar pagina
from django.urls import reverse_lazy

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome','email']
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')
    
class ClientesListagem(ListView):
    model = Clientes 
    template_name = 'cadastros/listar_cadastros.html'
    
def abertura_modelform(request):
    return render(request, "index.html")
