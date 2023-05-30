from django import forms
from .models import Category, Recipe, Comment

INPUT_CLASS = 'form-control py-2 px-3'

class newRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients', 'directions', 'category', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'es. Pizza Margherita',
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'es. Best pizza ever',
                'class': INPUT_CLASS,
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'es. 1 cup of flour, 1 cup of water, 1 cup of salt',
                'class': INPUT_CLASS,
            }),
            'directions': forms.Textarea(attrs={
                'placeholder': 'es. 1. Mix the flour, water and salt in a bowl. 2. Bake for 30 minutes',
                'class': INPUT_CLASS,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            })
        }


class editRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients', 'directions', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'es. Pizza Margherita',
                'class': INPUT_CLASS,
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'es. Best pizza ever',
                'class': INPUT_CLASS,
            }),
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'es. 1 cup of flour, 1 cup of water, 1 cup of salt',
                'class': INPUT_CLASS,
            }),
            'directions': forms.Textarea(attrs={
                'placeholder': 'es. 1. Mix the flour, water and salt in a bowl. 2. Bake for 30 minutes',
                'class': INPUT_CLASS,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'class': INPUT_CLASS,
            })
        }
