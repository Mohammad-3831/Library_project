from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from . import settings
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Library Project",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',include('Book.urls')),
    path('accounts/',include('Users.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
