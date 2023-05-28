from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Recipe
from django.contrib.auth.decorators import login_required
from .forms import newRecipeForm

# Create your views here.

def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(pk=pk)[0:4]

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'related_recipes': related_recipes
    })

@login_required
def addRecipe(request):
    if request.method == 'POST':
        form = newRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe:detail', pk=recipe.pk)
        else:
            form = newRecipeForm()

    return render(request, 'recipe/addRecipe.html', {
        'form': form
    })

