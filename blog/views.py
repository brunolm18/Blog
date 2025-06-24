
from rest_framework import generics
from blog.models import Autor,Categoria,Post
from rest_framework import status
from blog.serializers import AutorSerializer,CategoriaSerializer,PostSerializer,UserSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets



#Paginacion global para modelos
class PaginatorModels(PageNumberPagination):
    page_size = 10


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


    
    



class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [permissions.AllowAny]
    pagination_class = PaginatorModels
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'autor']  # Filtrar por estos campos exactos
    search_fields = ['title', 'description', 'text']  # Buscar por texto en estos campos
    ordering_fields = ['date', 'title']
     

    
    
    

    def http_method_not_allowed(self, request,*args,**kwargs):
        return Response(data={"error":f'Metodo {request.method} no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED,)
    
    def list(self, request,*args,**kwargs):
       queryset = self.get_queryset()
       serializer = self.get_serializer(queryset,many=True)
       return Response({
           "total":queryset.count(),
           "posts":serializer.data
       })

    



    
    
    

    

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]




class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    

class AutorList(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PaginatorModels


    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response(content_type=f"Metodo {request.method } no permitido",status=405)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AutorDetail(generics.RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.AllowAny]
    

class AutorCreate(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginatorModels

class AutorUpdate(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class AutorDelete(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]
 

class CategoriaList(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PaginatorModels


class CategoriaDetail(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination

class CategoriaCreate(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    

class CategoriaUpdate(generics.UpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    


class CategoriaDelete(generics.DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    