from rest_framework import serializers
from blog.models import Autor,Categoria,Post
from django.contrib.auth.models import User
class AutorSerializer(serializers.ModelSerializer): #Serializer de Autor
    class Meta:
        model = Autor
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer): #Serializer de Categoria
    class Meta:
        model = Categoria
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer): #Serializer de Posts
    class Meta:
        model = Post
       
        fields = "__all__"
        
        

        
