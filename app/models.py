import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, CASCADE, ManyToManyField


class Region(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Tag(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtaglar'


class Blog(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=55)
    text = RichTextUploadingField()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('app.Category', CASCADE)
    region = ForeignKey('app.Region', CASCADE, null=True, blank=True)
    author = ForeignKey('auth.User', CASCADE)
    tag = ManyToManyField('app.Tag')

    def __str__(self):
        return self.title
