# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    
    list_display = ('pk','user','title','photo','created')
    list_display_links = ('pk','user','title')
    list_filter = ('user','created')

    search_fields = ('user__username','title')

    readonly_fields = ('created','modified')