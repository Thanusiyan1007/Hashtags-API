import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY  # Ensure API key is set in settings.py

def generate_hashtags(post_caption):
    try:
        prompt = f"Generate the best SEO-friendly meta keywords for this post: {post_caption}. Provide only the keywords without symbols. Ensure they are optimized for search engines and social media engagement."

        response = openai.chat.completions.create(  # ✅ Correct OpenAI method
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        hashtags = response.choices[0].message.content
        print("Generated Hashtags:", hashtags)  # ✅ Debugging

        if not hashtags:
            return []

        return hashtags.split()
    
    except Exception as e:
        print(f"OpenAI API Error: {e}")  # ✅ Log errors for debugging
        return []
