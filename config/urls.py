from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.api import router

schema_view = get_schema_view(
    openapi.Info(
        title="Fast Food Delivery API",
        default_version="v1",
        description="Fast Food Delivery ",
        terms_of_service="#",
        # Change e-mail on this line!
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),

    path('api/', include(router.urls)),
]
