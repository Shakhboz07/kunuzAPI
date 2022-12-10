from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, SlugField, CharField, TextField, DateTimeField, \
    ImageField, ForeignKey, CASCADE, SET_NULL
from django.utils.text import slugify


# Create your models here.

class Category(Model):
    name = CharField(max_length=200)
    slug = SlugField(max_length=255, unique=True)
    tag = ArrayField(CharField(max_length=255), null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Region(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    tag = ArrayField(CharField(max_length=255), null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Region.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(Model):
    author = ForeignKey('auth.User', CASCADE)
    region = ForeignKey('app.Region', SET_NULL, null=True)
    title = CharField(max_length=255)
    descriptions = CharField(max_length=255)
    image = ImageField(upload_to='category/images/')
    text = TextField()
    slug = SlugField(max_length=255, unique=True)
    tag = ArrayField(CharField(max_length=255), null=True)

    created_at = DateTimeField(auto_now=True)
    update_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Blog.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
