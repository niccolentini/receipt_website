from django.contrib import admin
from .models import Category, Recipe, LikeRecipe, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(LikeRecipe)
admin.site.register(Comment)
