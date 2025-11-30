from django.urls import include, path
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from api.v1.views.user_view import UserViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version='v1',
        description="API from Task",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", include(v1_router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    

]



