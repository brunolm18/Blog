from rest_framework import generics, viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from blog.models import Author, AuthorProfile, Category, Post, Tag
from blog.serializers import AuthorSerializer, CategorySerializer, PostSerializer, TagSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from blog.service.post_service import get_latest_active_posts  
from rest_framework.views import APIView
from rest_framework.response import Response

class Pagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = "page_size"
    max_page_size = 20
    invalid_page_message = "Invalid page. Go through a valid page."


@extend_schema(summary="CRUD for Authors", tags=["Authors"])
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(summary="CRUD for Categories", tags=["Categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(summary="CRUD for Tags", tags=["Tags"])
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(summary="CRUD for Posts", tags=["Posts"])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author', 'category').prefetch_related('tags').order_by('-pub_date')
    serializer_class = PostSerializer
    pagination_class = Pagination
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'category__name', 'author__username', 'status']


    @method_decorator(cache_page(60*5))  # cac
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema(summary="Servicio: Últimos posts publicados", tags=["Servicios"])
class LatestPostsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        posts = get_latest_active_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)