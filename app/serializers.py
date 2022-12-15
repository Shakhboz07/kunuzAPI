from rest_framework.serializers import ModelSerializer

from app.models import Blog, Category, Region, Tag


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('author', 'region')


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
