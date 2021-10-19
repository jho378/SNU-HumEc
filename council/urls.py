from django.urls import path
from . import views

app_name = "council"

urlpatterns = [
    path("about/", views.council_about, name="council_about"),
    path("rule/", views.council_rule, name="council_rule"),
    path("conference/", views.council_conference, name="council_conference"),
    path("minutes/", views.council_minutes, name="council_minutes"),
]
