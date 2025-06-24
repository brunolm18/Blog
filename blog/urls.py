from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import AuthorViewSet, CategoryViewSet, PostViewSet, TagViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
