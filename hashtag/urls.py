from django.urls import path
from .views import GetTrendingHashtagsView, GenerateHashtagsView, SaveHashtagView

urlpatterns = [
    path('trending/', GetTrendingHashtagsView.as_view(), name="trending_hashtags"),
    path('generate/', GenerateHashtagsView.as_view(), name="generate_hashtags"),
    path('save/', SaveHashtagView.as_view(), name="save_hashtag"),
]
