from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Poke Api Search V1",
      default_version='v1',
      description="Backend developer test by osw4l",
      contact=openapi.Contact(email="ioswxd@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('apps.pokedex.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

