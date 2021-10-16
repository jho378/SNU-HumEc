from django.urls import path
from . import views

app_name = "council"

urlpatterns = [
    path("about/", views.council_about, name="council_about"),
]
