from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Tag, Post, PostTag
from post.serializers import PostSerializer


class MyTestCase(TestCase):
    post = None

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='user', password='12345678')
        tag1 = Tag.objects.create(name='tag1')
        tag2 = Tag.objects.create(name='tag2')
        tag3 = Tag.objects.create(name='tag3')
        cls.post = Post.objects.create(title='title',
                                       contents='contents',
                                       owner=user)
        PostTag.objects.create(post=cls.post, tag=tag1)
        PostTag.objects.create(post=cls.post, tag=tag2)
        PostTag.objects.create(post=cls.post, tag=tag3)

    def test_total_cnt_for_post_tag(self):
        serializer = PostSerializer(instance=self.post)
        print(serializer.get_post_tags(self.post))
        self.assertEqual(len(serializer.get_post_tags(self.post)), 3)