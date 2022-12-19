import pytest
from faker import Faker
from model_bakery import baker

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
