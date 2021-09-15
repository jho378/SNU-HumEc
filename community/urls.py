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
    path("delete/<int:pk>/", views.community_delete, name="community_delete"),
]
