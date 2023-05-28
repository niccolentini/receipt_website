from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Recipe
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import newRecipeForm, editRecipeForm

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


@login_required
def deleteRecipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    recipe.delete()

    return redirect('dashboard:dashboardPage')


@login_required
def editRecipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = editRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe.save()
            return redirect('recipe:detail', pk=recipe.pk)
    else:
            form = editRecipeForm(instance=recipe)

    return render(request, 'recipe/editRecipe.html', {
        'form': form
    })

def searchRecipe(request):
    query = request.GET.get('query', '')
    recipes = Recipe.objects.all()

    if query:
        recipes = Recipe.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'recipe/searchRecipe.html', {
        'recipes': recipes,
        'query': query,
    })