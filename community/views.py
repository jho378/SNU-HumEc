from django.shortcuts import render, redirect
from .models import CommunityPost, CommunityComment


def get_board(board_en):
    board_dict = {"market": "장터 게시판",
                  "promotion": "홍보 게시판",
                  "free": "자유 게시판",
                  "study": "스터디/강의 게시판"}
    return board_dict[board_en]


def get_list_ctx(board_en, board_ko):
    queryset = CommunityPost.objects.filter(board=board_en)
    ctx = {
        "board": board_ko,
        "posts": queryset,
    }
    return ctx


def market_list(request):
    ctx = get_list_ctx("market", "장터 게시판")
    return render(request, "community/community_list.html", ctx)


def promotion_list(request):
    ctx = get_list_ctx("promotion", "홍보 게시판")
    return render(request, "community/community_list.html", ctx)


def free_list(request):
    ctx = get_list_ctx("free", "자유 게시판")
    return render(request, "community/community_list.html", ctx)


def study_list(request):
    ctx = get_list_ctx("study", "스터디/강의 게시판")
    return render(request, "community/community_list.html", ctx)


def community_detail(request, pk):
    queryset = CommunityPost.objects.get(pk=pk)
    comments = CommunityComment.objects.filter(post=queryset)
    board = get_board(queryset.board)
    login_user = request.user
    is_post_user = True if queryset.user == login_user else False

    if request.method == "POST":
        post = queryset
        contents = request.POST["contents"]
        user = request.user
        CommunityComment.objects.create(post=post, contents=contents, user=user)
        return redirect("community:community_detail", pk)

    ctx = {
        "board": board,
        "post": queryset,
        "comments": comments,
        "login_user": login_user,
        "is_post_user": is_post_user,
    }
    return render(request, "community/community_detail.html", ctx)
