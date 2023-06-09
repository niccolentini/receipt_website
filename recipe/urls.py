from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('addRecipe/', views.addRecipe, name='addRecipe'),
    path('<int:pk>/delete/', views.deleteRecipe, name='deleteRecipe'),
    path('<int:pk>/edit/', views.editRecipe, name='editRecipe'),
    path('search/', views.searchRecipe, name='searchRecipe'),
    path('<int:pk>/likeRecipe/', views.likeRecipe, name='likeRecipe'),
    path('likedRecipes/', views.likedRecipes, name='likedRecipes'),
    path('deleteComment/<int:pk>/', views.deleteComment, name='deleteComment')
]