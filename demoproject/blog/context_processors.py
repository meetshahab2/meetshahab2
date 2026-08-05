# blog/context_processors.py

from .models import Post

def latest_posts(request):
    posts = (
        Post.objects
        .filter(is_published=True)
        .order_by('-created_at')[:5]
    )
    return {
        'latest_posts': posts,
    }

# Create your global menu here.
