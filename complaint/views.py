from django.shortcuts import render, redirect
from .models import Complaint, ComplaintComment


def complaint_list(request):
    queryset = Complaint.objects.all()
    login_user = request.user
    ctx = {
        "posts": queryset,
        "login_user": login_user,
    }
    return render(request, "complaint/complaint_list.html", ctx)


def complaint_detail(request, pk):
    queryset = Complaint.objects.get(pk=pk)
    is_post_user = True if queryset.user == request.user else False
    ctx = {
        "post": queryset,
        "is_post_user": is_post_user,
    }
    return render(request, "complaint/complaint_detail.html", ctx)