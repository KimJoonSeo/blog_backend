from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Tag, Post, PostTag, Comment
from post.serializers import PostSerializer


class PostSerializerTestClass(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='user', password='12345678')
        tag1 = Tag.objects.create(name='tag1')
        tag2 = Tag.objects.create(name='tag2')
        tag3 = Tag.objects.create(name='tag3')

        self.post = Post.objects.create(title='title',
                                       contents='contents',
                                       owner=user)

        PostTag.objects.create(post=self.post, tag=tag1)
        PostTag.objects.create(post=self.post, tag=tag2)
        PostTag.objects.create(post=self.post, tag=tag3)

        Comment.objects.create(owner=user, post=self.post, contents='comment1')
        Comment.objects.create(owner=user, post=self.post, contents='comment2')

        self.serializer = PostSerializer(instance=self.post)

    def test_total_cnt_of_post_tags(self):
        self.assertEqual(len(self.serializer.get_post_tags(self.post)), len(PostTag.objects.all()))

    def test_total_cnt_of_comments(self):
        self.assertEqual(self.serializer.get_cnt_of_comments(self.post), len(Comment.objects.all()))