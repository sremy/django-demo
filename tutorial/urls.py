"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from tutorial.quickstart import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

drf_schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="API description",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('manual/', views.ManualView.as_view()),
	path('generic/', views.GenericView.as_view()),
    path('rest-swagger/', get_swagger_view(title='Users API')),
    re_path(r'^drf-yasg-swagger(?P<format>\.json|\.yaml)$', drf_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('drf-yasg-swagger/', drf_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('drf-yasg-redoc/', drf_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	re_path('report/.*', views.ReportView.as_view()),
]
