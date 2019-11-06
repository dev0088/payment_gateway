from django.urls import path, reverse
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static, serve
from django.contrib.auth.views import LoginView, logout_then_login
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from .views import index, app, home

swagger_schema_view = get_swagger_view(title='Zap API')

schema_view = get_schema_view(
   openapi.Info(
      title="Zap API",
      default_version='v1',
      description="REST API for Zap web and mobile app",
      terms_of_service="hhttps://zapbackend.herokuapp.com/termsofservice/",
      contact=openapi.Contact(email="administrator@zap.com"),
      license=openapi.License(name="zap.com"),
   ),
   # validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API urls
    url(r'^apis(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^apis/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger-docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  
    url(r'^api/v1/payment/', include('payment_settings.urls')),
    # Admin urls
    path('admin/', admin.site.urls),
    # Default urls
    # path('/', index)  
   #  url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    url(r'^app/', app, name='app'),
    url('^auth/logout/$', logout_then_login, name='logout'),
    url('^auth/', index, name='auth'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
    url(r'^$', app, name='app')
]
