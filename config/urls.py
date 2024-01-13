from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Fast Food Delivery API",
        default_version="v1",
        description="Fast Food Delivery ",
        terms_of_service="#",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

security = [
    {
        "Bearer Token": [],
    },
    {
        "Basic Auth": [],
    },
]


def custom_get_schema_view(*args, **kwargs):
    result = schema_view(*args, **kwargs)
    result._security = security  # Set custom security requirements
    return result


urlpatterns = [
    path('admin/', admin.site.urls),

    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger",
                                         cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
                                       cache_timeout=0), name="schema-redoc"),

    path('', include("main.urls")),
]
