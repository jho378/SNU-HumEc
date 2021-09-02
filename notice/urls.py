from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path("", views.notice_list, name="notice_list"),
    path("<int:pk>/", views.notice_detail, name="notice_detail"),
    path("create/", views.notice_create, name="notice_create"),
    path("update/<int:pk>/", views.notice_update, name="notice_update"),
    path("delete/<int:pk>/", views.notice_delete, name="notice_delete"),
]
