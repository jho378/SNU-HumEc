from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django import core

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls")),
    path("major/", include("major.urls")),
    path("accounts/", include("accounts.urls")),
    path("notice/", include("notice.urls")),
    path("complaint/", include("complaint.urls")),
    path("community/", include("community.urls")),
    path("council/", include("council.urls")),
    path("", lambda req: redirect("core:core")),
]
