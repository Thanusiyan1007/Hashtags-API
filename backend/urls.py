from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Debug view for root URL
def home(request):
    return JsonResponse({"message": "Welcome to Hashtags API!"})

urlpatterns = [
    path("", home),  # Add this route for "/"
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),      # Users API
    path("api/hashtags/", include("hashtag.urls")), # Hashtags API
]
