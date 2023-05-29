from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Recipe, LikeRecipe
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

@login_required
def likeRecipe(request, pk):
    username = request.user.username
    recipe_id = pk

    recipe = Recipe.objects.get(id=recipe_id)

    like_filter = LikeRecipe.objects.filter(recipe_id=recipe_id, username=username).first()

    if not like_filter:
        like = LikeRecipe.objects.create(recipe_id=recipe_id, username=username)
        like.save()
        recipe.n_of_likes += 1
        recipe.save()
        return redirect('/recipes/' + str(recipe_id) + '/')
    else:
        like_filter.delete()
        recipe.n_of_likes -= 1
        recipe.save()
        return redirect('/recipes/' + str(recipe_id) + '/')


@login_required
def likedRecipes(request):
    username = request.user.username
    recipes = LikeRecipe.objects.filter(username=username)
    liked_recipes = Recipe.objects.filter(id__in=recipes.values_list('recipe_id', flat=True))
    all_recipes = Recipe.objects.exclude(id__in=liked_recipes.values_list('id', flat=True)).order_by('?')

    return render(request, 'recipe/likedRecipes.html', {
        'liked_recipes': liked_recipes,
        'all_recipes': all_recipes,
    })
