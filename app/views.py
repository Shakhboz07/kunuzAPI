from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.filters import BlogFilter, RegionFilter, TagFilTer
from app.models import Category, Blog, Region, Tag
from app.serializers import CategoryModelSerializer, RegionModelSerializer, BlogModelSerializer, TagModelSerializer


# Create your views here.

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class RegionModelViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    filterset_class = RegionFilter


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    filterset_class = BlogFilter


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    filterset_class = TagFilTer
