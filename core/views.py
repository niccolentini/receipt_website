from django.shortcuts import render
from django.http import HttpResponse
from recipe.models import category, recipe
# Create your views here.



def homePage(request):
    recipes = recipe.objects.all()
    categorys = category.objects.all()
    return render(request, 'core/homePage.html', {
        'recipes': recipes,
        'categorys': categorys,
    })

def aboutPage(request):
    return render(request, 'core/aboutPage.html')