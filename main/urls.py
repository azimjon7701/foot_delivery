from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from main import views

staff_router = DefaultRouter()
staff_router.register(r'food', views.FoodViewSet, basename='food')
staff_router.register(r'order', views.OrderViewSet, basename='order')


customer_router = DefaultRouter()
customer_router.register(r'foods-for-customers', views.FoodReadOnlyViewSet, basename='food read-only')

urlpatterns = [
    path('staff/', include(staff_router.urls)),
    path('customer/', include(customer_router.urls)),
    path('auth/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('auth/login/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
]