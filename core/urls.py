"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import include, path
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', include('home.urls')),
#     path("admin/", admin.site.urls),
#     path("", include('admin_adminlte.urls'))
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter
from .views import ParamViewSet, CommentViewSet, SysOptionViewSet

router = DefaultRouter()
router.register(r'params', ParamViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'sysoptions', SysOptionViewSet)

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_adminlte.urls')),
    path('api/', include(router.urls)),
    # Получение схемы в формате JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Интерактивный UI Swagger
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
