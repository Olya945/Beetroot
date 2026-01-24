from django.shortcuts import render
from .models import Color, Recipe

def color_list(request):
    """Показує список всіх кольорів"""
    colors = Color.objects.all().order_by("name")
    return render(request, "colors/color_list.html", {"colors": colors})

def recipe_list(request):
    """Показує всі рецепти змішування"""
    recipes = Recipe.objects.all().order_by("result__name")
    return render(request, "colors/recipe_list.html", {"recipes": recipes})

def color_mixer(request):
    """Форма для змішування кольорів"""

    pass
