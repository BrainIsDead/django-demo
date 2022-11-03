from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('work_cards.urls')),
    # drf-spectacular
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="spectacular-schema"),
    path("api/docs/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="spectacular-schema"), name="spectacular-swagger-ui"),
    path("api/docs/schema/redoc/", SpectacularRedocView.as_view(url_name="spectacular-schema"), name="spectacular-redoc"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
