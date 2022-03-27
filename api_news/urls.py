from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api_news.views import PostViewSet

app_name = "api_news"

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "post/<int:pk>/up_vote/",
        PostViewSet.as_view({"get": "up_vote"}, basename="up_vote"),
    ),
    path(
        "post/<int:pk>/add_comment/",
        PostViewSet.as_view({"post": "add_comment"}, basename="add_comment"),
    ),
]

urlpatterns += router.urls
