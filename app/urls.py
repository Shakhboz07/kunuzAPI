from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views import CategoryModelViewSet, RegionModelViewSet, BlogModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, basename='category')
router.register('region', RegionModelViewSet, basename='region')
router.register('blog', BlogModelViewSet, basename='blog')

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
