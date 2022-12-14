from django.contrib import admin

from app.models import Blog, Category, Region, Tag


# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    exclude = ('slug',)
