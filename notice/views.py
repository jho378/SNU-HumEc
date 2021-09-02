from django.shortcuts import render
from .models import Notice


def notice_list(request):
    queryset = Notice.objects.all()
    ctx = {
        "posts": queryset,
    }
    return render(request, "notice/notice_list.html", ctx)
