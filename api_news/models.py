from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def amount_of_upvotes(self):
        return self.upvotes.all().count()

    def __str__(self):
        return self.title


class UpVote(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="upvotes", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [("post", "user")]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return f"Comment {self.content} by {self.author_name}"
