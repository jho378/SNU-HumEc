from django.shortcuts import render


def notice_list(request):
    return render(request, "notice/notice_list.html")
