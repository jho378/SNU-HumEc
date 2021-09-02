from django.shortcuts import render, redirect
from .models import Notice
from .forms import NoticeForm


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


def notice_create(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("notice:notice_list")
    else:
        form = NoticeForm()
    ctx = {
        "form": form,
    }
    return render(request, "notice/notice_create.html", ctx)


def notice_update(request, pk):
    queryset = Notice.objects.get(pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("notice:notice_detail", pk)
    else:
        form = NoticeForm(instance=queryset)
    ctx = {
        "form": form,
    }
    return render(request, "notice/notice_create.html", ctx)


def notice_delete(request, pk):
    queryset = Notice.objects.get(pk=pk)

    if request.method == "POST":
        queryset.delete()
        return redirect("notice:notice_list")
    return redirect("notice:notice_detail", pk)

