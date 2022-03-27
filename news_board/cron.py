from api_news.models import UpVote


def reset_post_upvotes():
    UpVote.objects.all().delete()
    return
