from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe_images', blank=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    n_of_likes = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class LikeRecipe(models.Model):
    recipe_id = models.CharField(max_length=500)
    username = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username