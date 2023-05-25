from django.contrib import admin
from core.models import Article

# Register your models here.

class adminArticle(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content', 'category', 'author']

admin.site.register(Article, adminArticle)
