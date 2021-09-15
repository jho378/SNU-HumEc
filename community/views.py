from django.shortcuts import render
from .models import CommunityPost


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
