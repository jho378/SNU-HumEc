from django.shortcuts import render


def community_market(request):
    return render(request, "community/community_list.html")
