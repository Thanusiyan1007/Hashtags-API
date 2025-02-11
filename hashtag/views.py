from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .models import Hashtag, UserHashtag
from .ai import generate_hashtags
from .scraper import save_trending_hashtags


class GetTrendingHashtagsView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication required

    def get(self, request):
        platform = request.GET.get("platform", "Instagram")
        hashtags = Hashtag.objects.filter(platform=platform).order_by("-trend_score")[:10]
        return Response({"hashtags": [tag.name for tag in hashtags]}, status=status.HTTP_200_OK)

class GenerateHashtagsView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication required

    def post(self, request):
        post_caption = request.data.get("caption")
        if not post_caption:
            return Response({"error": "Caption is required"}, status=status.HTTP_400_BAD_REQUEST)

        hashtags = generate_hashtags(post_caption)
        return Response({"hashtags": hashtags}, status=status.HTTP_200_OK)

class SaveHashtagView(APIView):
    permission_classes = [permissions.AllowAny]  # No authentication required

    def post(self, request):
        hashtag_name = request.data.get("hashtag")
        platform = request.data.get("platform", "Instagram")

        hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_name, platform=platform)
        UserHashtag.objects.create(user=None, hashtag=hashtag)  # No user required

        return Response({"message": "Hashtag saved successfully"}, status=status.HTTP_201_CREATED)
