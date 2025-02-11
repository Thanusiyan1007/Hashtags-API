from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse



urlpatterns = [
    path("", admin.site.urls),
    path("api/users/", include("users.urls")),      # Users API
    path("api/hashtags/", include("hashtag.urls")), # Hashtags API
]
