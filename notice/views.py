from django.shortcuts import render
from .models import Notice


def notice_list(request):
    queryset = Notice.objects.all()
    ctx = {
        "posts": queryset,
    }
    return render(request, "notice/notice_list.html", ctx)


def notice_detail(request, pk):
    queryset = Notice.objects.get(pk=pk)
    is_post_user = True if queryset.user == request.user else False
    ctx = {
        "post": queryset,
        "is_post_user": is_post_user,
    }
    return render(request, "notice/notice_detail.html", ctx)
