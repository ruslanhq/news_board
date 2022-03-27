from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api_news.models import Post, UpVote, Comment
from api_news.permissions import IsOwnerOrReadOnly
from api_news.serializers import (
    PostSerializer,
    PostUpdateSerializer,
    CommentSerializer,
    PostRetrieveSerializer,
)
from django.db import IntegrityError

from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return PostUpdateSerializer
        elif self.action == "add_comment":
            return CommentSerializer
        elif self.action == "retrieve":
            return PostRetrieveSerializer
        else:
            return PostSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        return super().get_permissions()

    @action(
        methods=["get"],
        detail=True,
        url_name="up_vote",
        permission_classes=[IsAuthenticated],
    )
    def up_vote(self, request, pk=None):
        user = self.request.user
        try:
            post = Post.objects.get(pk=pk)
            UpVote.objects.create(user=user, post=post)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=["post"],
        detail=True,
        url_name="add_comment",
        permission_classes=[IsAuthenticated],
    )
    def add_comment(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content = serializer.validated_data["content"]
        user = self.request.user
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Comment.objects.create(post=post, author_name=user, content=content)
        return Response(status.HTTP_201_CREATED)


class CommentViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Comment.objects.select_related("post").all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
