from django.contrib import admin
from .models import Category,Gallery
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('category_name','slug')
    prepopulated_fields = {'slug':['category_name'],}

class AdminGallery(admin.ModelAdmin):
    list_display = ('category','slug','images')
    prepopulated_fields = {'slug':['category'],}

admin.site.register(Category,AdminCategory)
admin.site.register(Gallery,AdminGallery)
