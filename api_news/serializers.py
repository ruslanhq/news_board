from rest_framework import serializers

from api_news.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    upvotes = serializers.CharField(source="amount_of_upvotes", read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "link",
            "author_name",
            "creation_date",
            "upvotes",
        )

    def create(self, validated_data):
        return Post.objects.create(
            author_name=self.context["request"].user, **validated_data
        )


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    author_name = serializers.StringRelatedField()

    class Meta:
        model = Comment
        exclude = ("id",)


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "link")


class PostRetrieveSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)
    upvotes = serializers.CharField(source="amount_of_upvotes", read_only=True)

    class Meta:
        model = Post
        exclude = ("id",)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)
