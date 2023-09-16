from rest_framework import serializers

from post.models import Post, PostTag, Comment


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ['tag']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_tags = serializers.SerializerMethodField()
    cnt_of_comments = serializers.SerializerMethodField()

    def get_post_tags(self, post):
        post_tags_qs = PostTag.objects.filter(post=post)
        return PostTagSerializer(post_tags_qs, many=True).data

    def get_cnt_of_comments(self, post):
        return Comment.objects.filter(post=post).count()

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
