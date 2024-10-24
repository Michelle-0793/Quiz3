from django.urls import path
from . import views

urlpatterns = [
    # URLs para Usuario
    path('usuarios/', views.UsuarioListCreate.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario-detail'),
    
]

"""
# URLs para Receta
path('recetas/', views.RecetaListCreate.as_view(), name='receta-list'),
path('recetas/<int:pk>/', views.RecetaDetail.as_view(), name='receta-detail'), 

# URLs para Categoria
path('categorias/', views.CategoriaListCreate.as_view(), name='categoria-list'),
path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'), 

# URLs para Comentarios
path('comentarios/', views.ComentarioListCreate.as_view(), name='comentario-list'),
path('comentarios/<int:pk>/', views.ComentarioDetail.as_view(), name='comentario-detail'),

"""