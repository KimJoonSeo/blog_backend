from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    contents = models.TextField(blank=False, null=False)
    owner = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    contents = models.TextField(blank=False, null=False)
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', related_name='comment', on_delete=models.CASCADE, )

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class PostTag(models.Model):
    post = models.ForeignKey('Post', related_name='post_tag', on_delete=models.CASCADE, )
    tag = models.ForeignKey('Tag', related_name='post_tag', on_delete=models.CASCADE, )

    def __str__(self):
        return self.post.title + '-' + self.tag.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields= ['post', 'tag'],
                name = 'post-tag composite key'
            )
        ]