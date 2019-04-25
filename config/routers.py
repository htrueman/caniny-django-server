from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.permissions import IsAdminUser


class CategorizedAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        if len(operation_keys) >= 1:
            operation_keys = operation_keys[1:]
        return super().get_tags(operation_keys)


schema_view = get_schema_view(
    openapi.Info(
      title="Caniny (K9 Digital)",
      default_version='v1',
    ),
    permission_classes=(IsAdminUser,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui(), name='docs'),

    path('api/<version>/', include('users.routers')),
    path('api/<version>/organizations/', include('organizations.routers')),
    path('api/<version>/animals/', include('animals.routers')),
] \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
