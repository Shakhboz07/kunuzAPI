from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Category, Blog, Region
from app.serializers import CategoryModelSerializer, RegionModelSerializer, BlogModelSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated,)


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Blog
        fields = ('category', 'region')
