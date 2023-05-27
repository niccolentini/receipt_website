from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import category, recipe


# Create your views here.

def detail(request, pk):
    recipe1 = get_object_or_404(recipe, pk=pk)

    return render(request, 'recipe/detail.html', {'recipe': recipe1}),
