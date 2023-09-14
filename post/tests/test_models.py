from django.contrib.auth.models import User
from django.test import TestCase

from post.models import Tag, Post, PostTag


# Create your tests here.
class PostModelTestClass(TestCase):
    user = None
    tag = None
    post = None
    post_tag = None

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345678')
        cls.tag = Tag.objects.create(name='testtag')
        cls.post = Post.objects.create(title='test title',
                                       contents='test contents',
                                       owner=cls.user)
        cls.post_tag = PostTag.objects.create(post=cls.post, tag=cls.tag)

    def test_unique_constraint_for_post_tag(self):
        err = None
        try:
            PostTag.objects.create(post=self.post, tag=self.tag)
        except Exception as e:
            err = e
        self.assertIsNotNone(err)


