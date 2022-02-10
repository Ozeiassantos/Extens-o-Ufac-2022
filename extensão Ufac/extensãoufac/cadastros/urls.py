from django.urls import path
from cadastros import views
from cadastros.views import ClientesCad, ClientesListagem

urlpatterns = [
    path('', views.abertura_modelform , name='index'),
    path('cadastros/', ClientesCad.as_view(), name='cadastro'),
    path('listagem/', ClientesListagem.as_view(), name='listagem'),
    
] 