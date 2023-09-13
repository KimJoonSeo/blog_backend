from django.contrib import admin

from post.models import Post, Comment, Tag, PostTag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostTag)