from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("market/", views.community_market, name="community_market"),
]
