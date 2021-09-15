from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("market/", views.market_list, name="market_list"),
    path("promotion/", views.promotion_list, name="promotion_list"),
    path("free/", views.free_list, name="free_list"),
    path("study/", views.study_list, name="study_list"),
    path("market/<int:pk>/", views.market_detail, name="market_detail"),
]
