from django.contrib import admin
from .models import Photo, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug', 'ordre']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'created_at']
    list_filter = ['categorie']
