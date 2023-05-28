from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('addRecipe/', views.addRecipe, name='addRecipe'),
    path('<int:pk>/delete/', views.deleteRecipe, name='deleteRecipe'),
    path('<int:pk>/edit/', views.editRecipe, name='editRecipe'),
    path('search/', views.searchRecipe, name='searchRecipe'),
]