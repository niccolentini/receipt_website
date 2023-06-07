from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboardPage(request):
    recipes = Recipe.objects.filter(created_by=request.user)
    allrecipes = Recipe.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'recipes': recipes,
        'allrecipes': allrecipes
    })

