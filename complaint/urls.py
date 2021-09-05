from django.urls import path
from . import views

app_name = "complaint"

urlpatterns = [
    path("", views.complaint_list, name="complaint_list"),
    path("<int:pk>", views.complaint_detail, name="complaint_detail"),
    path("comment-update/", views.complaint_comment_update, name="complaint_comment_update"),
    path("comment-delete/", views.complaint_comment_delete, name="complaint_comment_delete"),
]
