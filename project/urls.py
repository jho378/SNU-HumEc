from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django import core

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls")),
    path("major/", include("major.urls")),
    path("", lambda req: redirect("core:core")),
]
