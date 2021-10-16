from django.shortcuts import render


def council_about(request):
    ctx = {"council_name": "학생회 소개"}
    return render(request, "council/council_about.html", ctx)


