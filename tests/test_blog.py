from django.urls import reverse_lazy
from model_bakery import baker
import pytest
from faker import Faker
from rest_framework.reverse import reverse_lazy

from app.models import Blog


@pytest.mark.django_db
class TestBlogApiView:

    @pytest.fixture
    def blogs(self):
        fake = Faker()
        blog = baker.make(
            Blog,
            title=fake.title(),
            text=fake.text(),
            image=fake.image(),
            tag=fake.tag('app.Tag', make_m2m=True),
        )

    @pytest.fixture
    def blog(self):
        return reverse_lazy('app:blog-list')

    def test_blog_list(self, client, blog):
        url = reverse_lazy('blog-list')
        # url = '/api/v1/region/'
        response = client.get(url)
        assert response.status_code == 200

    def test_blog_create_api(self, client, blog):
        url = reverse_lazy('blog-list')
        data = {
            'name': 'hello'
        }
        response = client.post(url, data)
        assert response.status_code == 201
        assert response.data['name'] == data['name']
