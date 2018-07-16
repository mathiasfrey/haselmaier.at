from django.conf import settings

def hasel_settings(request):
    
    return {
        'BLOG_ACTIVE': getattr(settings, 'BLOG_ACTIVE', False)  
    }