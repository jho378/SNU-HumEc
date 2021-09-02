from django.shortcuts import render, redirect
from major.models import MajorPost
from .forms import MajorPostForm


def get_major(major_en):
    major_dict = {"food": "식품영양학과",
                  "clothing": "의류학과",
                  "consumer": "소비자학과",
                  "child": "아동가족학과"}
    return major_dict[major_en]


# list
def get_list_ctx(major_en, major_ko):
    queryset = MajorPost.objects.filter(major=major_en)
    ctx = {
        "major": major_ko,
        "posts": queryset,
    }
    return ctx


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


# detail
def major_detail(request, pk):
    queryset = MajorPost.objects.get(pk=pk)
    major = get_major(queryset.major)
    is_post_user = True if queryset.user == request.user else False  # 작성자 확인

    ctx = {
        "major": major,
        "post": queryset,
        "is_post_user": is_post_user,
    }
    return render(request, "major/major_detail.html", ctx)


# create
def food_create(request):
    MAJOR = "food"
    if request.method == "POST":
        form = MajorPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.major = MAJOR
            post.save()
            return redirect("major:food_list")
    else:
        form = MajorPostForm()

    major = get_major(MAJOR)
    ctx = {
        "form": form,
        "major": major,
    }
    return render(request, "major/major_create.html", ctx)


def clothing_create(request):
    MAJOR = "clothing"
    if request.method == "POST":
        form = MajorPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.major = MAJOR
            post.save()
            return redirect("major:clothing_list")
    else:
        form = MajorPostForm()

    major = get_major(MAJOR)
    ctx = {
        "form": form,
        "major": major,
    }
    return render(request, "major/major_create.html", ctx)


def consumer_create(request):
    MAJOR = "consumer"
    if request.method == "POST":
        form = MajorPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.major = MAJOR
            post.save()
            return redirect("major:consumer_list")
    else:
        form = MajorPostForm()

    major = get_major(MAJOR)
    ctx = {
        "form": form,
        "major": major,
    }
    return render(request, "major/major_create.html", ctx)


def child_create(request):
    MAJOR = "child"
    if request.method == "POST":
        form = MajorPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.major = MAJOR
            post.save()
            return redirect("major:child_list")
    else:
        form = MajorPostForm()

    major = get_major(MAJOR)
    ctx = {
        "form": form,
        "major": major,
    }
    return render(request, "major/major_create.html", ctx)

# def major_create(request, major_name):
#     title = request.POST["title"]
#     contents = request.POST["contents"]
#     user = request.POST["user"].get_name()
#     image = request.POST["image"]
#     file = request.POST["file"]
#
#     post = MajorPost.objects.create(
#         title=title,
#         contents=contents,
#         user=user,
#         image=image,
#         file=file,
#         major=major_name,
#         pin=False
#     )
#     return redirect("major_detail", post.pk)


# update
def major_update(request, pk):
    queryset = MajorPost.objects.get(pk=pk)
    major = get_major(queryset.major)

    if request.method == "POST":
        form = MajorPostForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("major:major_detail", pk)
    else:
        form = MajorPostForm(instance=queryset)
    ctx = {
        "form": form,
        "major": major,
    }
    return render(request, "major/major_create.html", ctx)
