from django.contrib.auth.models import User
from django.test import TestCase

from post.models import Tag, Post, PostTag


# Create your tests here.
class PostModelTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='12345678')
        self.tag = Tag.objects.create(name='tag')
        self.post = Post.objects.create(title='title',
                                       contents='contents',
                                       owner=self.user)
        self.post_tag = PostTag.objects.create(post=self.post, tag=self.tag)

    def test_unique_constraint_for_post_tag(self):
        err = None
        try:
            PostTag.objects.create(post=self.post, tag=self.tag)
        except Exception as e:
            err = e
        self.assertIsNotNone(err)


