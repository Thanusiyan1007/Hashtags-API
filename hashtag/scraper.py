import requests
from bs4 import BeautifulSoup
from .models import Hashtag

def get_trending_hashtags(platform):
    url = f"https://some-trending-hashtags-website.com/{platform.lower()}/"  # Example URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    hashtags = []
    for tag in soup.find_all("div", class_="hashtag-class"):  # Adjust HTML class
        name = tag.text.strip()
        hashtags.append(name)

    return hashtags

def save_trending_hashtags(platform):
    hashtags = get_trending_hashtags(platform)
    for tag in hashtags:
        Hashtag.objects.update_or_create(name=tag, platform=platform)
