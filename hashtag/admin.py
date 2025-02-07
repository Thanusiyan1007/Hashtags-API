from django.contrib import admin
from .models import Hashtag, UserHashtag

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'trend_score', 'created_at')
    search_fields = ('name', 'platform')

@admin.register(UserHashtag)
class UserHashtagAdmin(admin.ModelAdmin):
    list_display = ('user', 'hashtag', 'saved_at')
    search_fields = ('user__username', 'hashtag__name')
