from django.contrib import admin
from .models import Photo, Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'date_ajout']
    list_filter = ['categorie']
