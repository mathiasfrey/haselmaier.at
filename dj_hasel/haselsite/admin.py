from django.contrib import admin
from models import BlogEntry, BlogTag, BlogImage, BlogAuthor

class BlogEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogEntry, BlogEntryAdmin)
    
    

class BlogTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogTag, BlogTagAdmin)


class BlogImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogImage, BlogImageAdmin)

class BlogAuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogAuthor, BlogAuthorAdmin)