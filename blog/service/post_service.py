from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from blog.models import Post
from blog.serializers import PostSerializer

@extend_schema(summary="Servicio: Últimos posts publicados", tags=["Servicios"])
class LatestPostsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        posts = Post.objects.filter(status='ACTIVE').order_by('-pub_date')[:5]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
