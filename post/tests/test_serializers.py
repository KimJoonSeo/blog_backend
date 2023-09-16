from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Tag, Post, PostTag, Comment
from post.serializers import PostSerializer


class PostSerializerTestClass(TestCase):
    post = None
    serializer = None

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

        Comment.objects.create(owner=user, post=cls.post, contents='comment1')
        Comment.objects.create(owner=user, post=cls.post, contents='comment2')

        cls.serializer = PostSerializer(instance=cls.post)

    def test_total_cnt_of_post_tags(self):
        self.assertEqual(len(self.serializer.get_post_tags(self.post)), 3)

    def test_total_cnt_of_comments(self):
        self.assertEqual(self.serializer.get_cnt_of_comments(self.post), 2)