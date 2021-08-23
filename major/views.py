from django.shortcuts import render
from major.models import MajorPost


def consumer_list(request):
    queryset = MajorPost.objects.filter(major="consumer")
    ctx = {
        "posts": queryset
    }
    return render(request, "major/consumer_list.html", ctx)
