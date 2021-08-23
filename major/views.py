from django.shortcuts import render
from major.models import MajorPost


def get_ctx(major_en, major_ko):
    queryset = MajorPost.objects.filter(major=major_en)
    ctx = {
        "major": major_ko,
        "posts": queryset,
    }
    return ctx


def food_list(request):
    ctx = get_ctx("food", "식품영양학과")
    return render(request, "major/major_list.html", ctx)


def clothing_list(request):
    ctx = get_ctx("clothing", "의류학과")
    return render(request, "major/major_list.html", ctx)


def consumer_list(request):
    ctx = get_ctx("consumer", "소비자학과")
    return render(request, "major/major_list.html", ctx)


def child_list(request):
    ctx = get_ctx("child", "아동가족학과")
    return render(request, "major/major_list.html", ctx)
