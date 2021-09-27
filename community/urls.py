from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("market/", views.market_list, name="market_list"),
    path("promotion/", views.promotion_list, name="promotion_list"),
    path("free/", views.free_list, name="free_list"),
    path("study/", views.study_list, name="study_list"),
    path("<int:pk>/", views.community_detail, name="community_detail"),
    path("create/market/", views.market_create, name="market_create"),
    path("create/promotion/", views.promotion_create, name="promotion_create"),
    path("create/free/", views.free_create, name="free_create"),
    path("create/study/", views.study_create, name="study_create"),
    path("update/market/<int:pk>/", views.market_update, name="market_update"),
    path("update/<int:pk>/", views.community_update, name="community_update"),
    path("delete/<int:pk>/", views.community_delete, name="community_delete"),
    path("comment-update/", views.community_comment_update, name="community_comment_update"),
    path("comment-delete/", views.community_comment_delete, name="community_comment_delete"),
]
