from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='Cursos',
        default_version='1.0.0',
        description='API documentation'
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='help/')),
    path('accounts/', include("accounts.urls")),
    path('cursos/', include("cursos.urls")),
    path('help/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
