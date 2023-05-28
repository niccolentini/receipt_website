from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipe.models import Category, Recipe
from .forms import SignupForm
# Create your views here.



def homePage(request):
    recipes = Recipe.objects.all()
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