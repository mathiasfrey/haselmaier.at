from django.contrib import admin
from models import Gallery, Category, Picture
from sorl.thumbnail.admin import AdminImageMixin

class PictureAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class GalleryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
