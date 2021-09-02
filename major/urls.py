from django.urls import path
from . import views

app_name = "major"

urlpatterns = [
    path("food/", views.food_list, name="food_list"),
    path("clothing/", views.clothing_list, name="clothing_list"),
    path("consumer/", views.consumer_list, name="consumer_list"),
    path("child/", views.child_list, name="child_list"),
    path("<int:pk>/", views.major_detail, name="major_detail"),
    path("create/food/", views.food_create, name="food_create"),
    path("create/clothing/", views.clothing_create, name="clothing_create"),
    path("create/consumer/", views.consumer_create, name="consumer_create"),
    path("create/child/", views.child_create, name="child_create"),
    path("update/<int:pk>/", views.major_update, name="major_update"),
    path("delete/<int:pk>/", views.major_delete, name="major_delete"),
]
