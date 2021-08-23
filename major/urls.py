from django.urls import path
from . import views

app_name = "major"

urlpatterns = [
    path("consumer", views.consumer_list, name="consumer_list"),
]
