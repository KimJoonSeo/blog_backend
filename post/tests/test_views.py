import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from post.models import Tag, Post, PostTag


class PostAPIViewTestCase(APITestCase):
    auth_token_url = reverse("auth:token")
    post_list_url = reverse("post:list")
    post_detail_url = reverse("post:detail", kwargs={"pk": 1})
    def setUp(self):
        self.username = "john"
        self.username2 = "park"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.user2 = User.objects.create_user(self.username2, self.email, self.password)
        self.tag = Tag.objects.create(name='tag')
        self.tag2 = Tag.objects.create(name='tag2')
        self.post = Post.objects.create(title='title',
                                        contents='contents',
                                        owner=self.user)
        self.post_id = self.post.id
        self.post2 = Post.objects.create(title='title2',
                                        contents='contents',
                                        owner=self.user)
        self.post_tag = PostTag.objects.create(post=self.post, tag=self.tag)
        self.post_tag2 = PostTag.objects.create(post=self.post2, tag=self.tag2)
        self.auth_info = {
            'username':self.username,
            'password': self.password
        }
        r = self.client.post(self.auth_token_url, self.auth_info)
        self.access_token1 =  r.data['access']
        self.auth_info['username'] = self.username2
        r = self.client.post(self.auth_token_url, self.auth_info)
        self.access_token2 = r.data['access']

    def test_post_list_api(self):
        """
        Test to verify post list api
        """
        headers = {
            'Authorization': 'Bearer ' + self.access_token1
        }
        r = self.client.get(self.post_list_url, headers)
        self.assertEqual(200, r.status_code)
        posts = json.loads(r.content)
        self.assertEqual(len(posts), len(PostTag.objects.all()))
