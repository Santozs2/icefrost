from django.urls import path
from . import views 

urlpatterns = [

    # Index 

    path('', views.index, name = 'index'),

    # Autenticação

    path('cadastro/', views.cadastrarUsuario, name = 'cadastrarUsuario'),

    # Cardápio
    path('cardapio/', views.cardapio, name = 'cardapio'),

    # Comentarios
    path('comentarios/novo/', views.cadastrarComentario, name = 'cadastrarComentario'),
    path('comentarios/', views.listarComentario, name = 'listarComentario'),
    path('comentarios/<int:pk>/editar/', views.editarComentario, name = 'editarComentario'),
    path('comentarios/<int:pk>/excluir/', views.excluirComentario, name = 'excluirComentario'),

    # Sorvetes

    path('sorvetes/', views.listarSorvete, name = 'listarSorvete'),
    path('sorvetes/novo/', views.cadastrarSorvete, name = 'cadastrarSorvete'),
    path('sorvetes/<int:pk>/editar/', views.editarSorvete, name = 'editarSorvete'),
    path('sorvetes/<int:pk>/excluir/', views.excluirSorvete, name = 'excluirSorvete'),
    
    # Galeria
    path('galeria/', views.galeria, name='galeria'),
]