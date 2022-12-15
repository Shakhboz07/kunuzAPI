from django_filters import rest_framework as filters
from app.models import Blog, Region, Tag


class BlogFilter(filters.FilterSet):
    class Meta:
        model = Blog
        fields = ('region', 'author', 'tag')


class RegionFilter(filters.FilterSet):
    class Meta:
        model = Region
        fields = ('name',)


class TagFilTer(filters.FilterSet):
    class Meta:
        model = Tag
        fields = ('name',)
