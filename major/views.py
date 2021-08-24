from django.shortcuts import render
from major.models import MajorPost


def get_list_ctx(major_en, major_ko):
    queryset = MajorPost.objects.filter(major=major_en)
    ctx = {
        "major": major_ko,
        "posts": queryset,
    }
    return ctx


def get_major(major_en):
    major_dict = {"food": "식품영양학과",
                  "clothing": "의류학과",
                  "consumer": "소비자학과",
                  "child": "아동가족학과"}
    return major_dict[major_en]


def food_list(request):
    ctx = get_list_ctx("food", "식품영양학과")
    return render(request, "major/major_list.html", ctx)


def clothing_list(request):
    ctx = get_list_ctx("clothing", "의류학과")
    return render(request, "major/major_list.html", ctx)


def consumer_list(request):
    ctx = get_list_ctx("consumer", "소비자학과")
    return render(request, "major/major_list.html", ctx)


def child_list(request):
    ctx = get_list_ctx("child", "아동가족학과")
    return render(request, "major/major_list.html", ctx)


def major_detail(request, pk):
    queryset = MajorPost.objects.get(pk=pk)
    major = get_major(queryset.major)
    ctx = {
        "major": major,
        "post": queryset,
    }
    return render(request, "major/major_detail.html", ctx)
