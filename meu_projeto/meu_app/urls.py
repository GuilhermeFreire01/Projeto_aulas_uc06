from django.urls import path
from . import views  # Importe a view do seu app
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial do app
    path('contatos/', views.contatos, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('endereco/', views.endereco, name='endereco'),
    path('blog/', views.blog, name='blog'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar_pedido/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    path('cliente/excluir/<int:cliente_id>', views.excluir_cliente, name='excluir_cliente'),
    path('cliente/editar/<int:cliente_id>', views.editar_cliente, name='editar_cliente'),
    path('listar_pedido/', views.listar_pedido, name='listar_pedido'),
    path('listar_produto/', views.listar_produto, name='listar_produto'),
    path('excluir_pedido/<pk>', views.excluir_pedido, name='excluir_pedido'),
    path('excluir_produto/<pk>', views.excluir_produto, name='excluir_produto'),
]







#path('/sobre', views.sobre, name='sobre')