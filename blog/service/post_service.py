from blog.models import Post

def get_latest_active_posts(limit=5):
    return Post.objects.filter(status='ACTIVE').order_by('-pub_date')[:limit]
