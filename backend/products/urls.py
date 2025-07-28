from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, ProductViewSet

# Create URL patterns for API endpoints
router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]