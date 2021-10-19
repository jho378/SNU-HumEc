from django.shortcuts import render
from .models import CouncilPost


def council_about(request):
    ctx = {"council_name": "학생회 소개"}
    return render(request, "council/council_about.html", ctx)


def council_rule(request):
    queryset = CouncilPost.objects.filter(council="rule").filter(pin=False).order_by("-created_at")
    pin_council = CouncilPost.objects.filter(council="rule").filter(pin=True).order_by("-created_at")
    ctx = {
        "posts": queryset,
        "pin_posts": pin_council,
        "council_name": "회칙 / 세칙"
    }
    return render(request, "council/council_list.html", ctx)


def council_conference(request):
    queryset = CouncilPost.objects.filter(council="conference").filter(pin=False).order_by("-created_at")
    pin_council = CouncilPost.objects.filter(council="conference").filter(pin=True).order_by("-created_at")
    ctx = {
        "posts": queryset,
        "pin_posts": pin_council,
        "council_name": "생운위 / 전학대회"
    }
    return render(request, "council/council_list.html", ctx)


def council_minutes(request):
    queryset = CouncilPost.objects.filter(council="minutes").filter(pin=False).order_by("-created_at")
    pin_council = CouncilPost.objects.filter(council="minutes").filter(pin=True).order_by("-created_at")
    ctx = {
        "posts": queryset,
        "pin_posts": pin_council,
        "council_name": "학생회 회의록"
    }
    return render(request, "council/council_list.html", ctx)
