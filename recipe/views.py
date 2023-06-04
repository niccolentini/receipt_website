from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Recipe, LikeRecipe, Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import newRecipeForm, editRecipeForm, CommentForm

# Create your views here.

def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(pk=pk)[0:4]
    comments = Comment.objects.filter(recipe=recipe).order_by('-date')
    allrecipes = Recipe.objects.all()
    liked_rec = LikeRecipe.objects.filter(username=request.user.username, recipe_id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.user = None
            comment.recipe = recipe
            comment.save()
            return redirect('recipe:detail', pk=recipe.pk)
    else:
        form = CommentForm()

    return render(request, 'recipe/detail.html', {
        'recipe': recipe,
        'related_recipes': related_recipes,
        'form': form,
        'comments': comments,
        'allrecipes': allrecipes,
        'liked_rec': liked_rec
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
    allrecipes = Recipe.objects.all()

    if query:
        recipes = Recipe.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'recipe/searchRecipe.html', {
        'recipes': recipes,
        'query': query,
        'allrecipes': allrecipes
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
    allrecipes = Recipe.objects.all()

    return render(request, 'recipe/likedRecipes.html', {
        'liked_recipes': liked_recipes,
        'all_recipes': all_recipes,
        'allrecipes': allrecipes
    })

@login_required
def deleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    recipe_pk = comment.recipe.pk
    comment.delete()

    return redirect('recipe:detail', pk=recipe_pk)

