from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Recipe


# Create your views here.

def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(pk=pk)[0:4]

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'related_recipes': related_recipes
    })

