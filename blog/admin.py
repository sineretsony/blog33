from django.contrib import admin
from .models import Post, Category, Comment, Tag, Newsletter # new

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Newsletter)