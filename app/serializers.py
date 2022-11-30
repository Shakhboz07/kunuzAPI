from rest_framework.serializers import ModelSerializer

from app.models import Blog, Category, Region


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('slug', 'author', 'region')


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug',)


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('slug',)
