
from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import  SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    

    path('api/schema',SpectacularAPIView.as_view(),name='schema'),
    path('api/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('api/schema/redoc/',SpectacularRedocView.as_view(),name='redoc'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

