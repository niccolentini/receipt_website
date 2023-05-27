from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe_images', blank=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
