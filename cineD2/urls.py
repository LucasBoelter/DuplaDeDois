from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home_app.urls")),
    path('em_cartaz/', include("cartaz_app.urls")),
    path('assentos/', include("assentos_app.urls")),
    path('usuario/', include("usuario_app.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)