from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipe.models import Category, Recipe
from .forms import SignupForm
from django.contrib.auth import logout

# Create your views here.

def homePage(request):
    recipes = Recipe.objects.all().order_by('?')
    categorys = Category.objects.all()
    return render(request, 'core/homePage.html', {
        'recipes': recipes,
        'categorys': categorys,
    })

def aboutPage(request):
    return render(request, 'core/aboutPage.html')

def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            form = SignupForm()



    form = SignupForm()
    return render(request, 'core/signupPage.html', {
        'form': form
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('core:homePage')

def categoryRecipes(request, pk):
    category = Category.objects.get(pk=pk)
    recipes = Recipe.objects.filter(category=category)

    return render(request, 'core/categoryRecipes.html', {
        'recipes': recipes,
        'category': category
    })