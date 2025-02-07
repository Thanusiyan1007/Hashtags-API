from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Hashtag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    platform = models.CharField(max_length=50, choices=[("Instagram", "Instagram"), ("Facebook", "Facebook")])
    trend_score = models.FloatField(default=0.0)  # Popularity score
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.platform})"

class UserHashtag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
