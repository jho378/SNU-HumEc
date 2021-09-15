from django.shortcuts import render
from notice.models import Notice
from community.models import CommunityPost


def core(request):
    notice_queryset = Notice.objects.all()
    market_queryset = CommunityPost.objects.filter(board="market")
    ctx = {
        "notice_posts": notice_queryset[:14],
        "market_posts": market_queryset[:14],
    }
    return render(request, "core/core.html", ctx)
