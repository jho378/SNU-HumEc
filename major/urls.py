from django.urls import path
from . import views

app_name = "major"

urlpatterns = [
    path("food", views.food_list, name="food_list"),
    path("clothing", views.clothing_list, name="clothing_list"),
    path("consumer", views.consumer_list, name="consumer_list"),
    path("child", views.child_list, name="child_list"),
    path("<int:pk>", views.major_detail, name="major_detail"),
]
