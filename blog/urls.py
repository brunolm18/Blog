from django.urls import path
from blog.views import *

urlpatterns = [
    #Posts urls
    path("",api_root,name="api_root"),
    path("posts",PostList.as_view(),name="posts"),
    path("posts/<int:pk>",PostDetail.as_view(),name="postsdetail"),
    path("posts_create",PostCreate.as_view(),name="posts_create"),
    path("posts/<int:pk>/update",PostUpdate.as_view(),name="posts_update"),
    path("posts/<int:pk>/delete",PostDelete.as_view(),name="posts_delete"),

    #Categorias_urls

    path("categorias",CategoriaList.as_view(),name="categorias"),
    path("categorias/<int:pk>",CategoriaDetail.as_view(),name="categorias_detail"),
    path("categorias_create",CategoriaCreate.as_view(),name="categorias_create"),
    path("categorias/<int:pk>/update",CategoriaUpdate.as_view(),name="categorias_update"),
    path("categorias/<int:pk>/delete",CategoriaDelete.as_view(),name="categorias_delete"),

    #Autores_urls
    path("autores",AutorList.as_view(),name="autores"),
    path("autores/<int:pk>",AutorDetail.as_view(),name="autores_detail"),
    path("autores_create",AutorCreate.as_view(),name="autores_create"),
    path("autores/<int:pk>/update",AutorUpdate.as_view(),name="autores_update"),
    path("autores/<int:pk>/delete",AutorDelete.as_view(),name="autores_delete"),
    
    


]