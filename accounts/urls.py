from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("done/", views.done, name="done"),
    path("login/", views.signin, name="login"),
]