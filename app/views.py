from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from app.models import Category, Blog, Region
from app.serializers import CategoryModelSerializer, RegionModelSerializer, BlogModelSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'tag']


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'tag']


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text', 'tag']
