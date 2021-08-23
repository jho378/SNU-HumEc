from django.shortcuts import render
from major.models import MajorPost


def consumer_list(request):
    queryset = MajorPost.objects.filter(major="consumer")
    ctx = {
        "major": "소비자학과",
        "posts": queryset,
    }
    return render(request, "major/major_list.html", ctx)
