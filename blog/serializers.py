from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, title):
        if Post.objects.filter(title=title).exists():
            raise serializers.ValidationError("Title already exists")
        else:
            return title
