from django.shortcuts import render
from .models import Color, Recipe

def home(request):
    return render(request, "colors/home.html")

def color_list(request):
    """Показує список всіх кольорів"""
    colors = Color.objects.all().order_by("name")
    return render(request, "colors/color_list.html", {"colors": colors})

def recipe_list(request):
    """Показує всі рецепти змішування"""
    recipes = Recipe.objects.all().order_by("result__name")
    return render(request, "colors/recipe_list.html", {"recipes": recipes})

def what_can_i_mix(request):
    """Показує що можна змішати з наявних кольорів"""
    all_colors = Color.objects.all().order_by("name")
    possible_recipes = []
    selected_colors = []

    if request.method == "POST":
        # Отримуємо ID вибраних кольорів
        selected_color_ids = [int(id) for id in request.POST.getlist("colors")]
        selected_colors = Color.objects.filter(id__in=selected_color_ids)

        # Шукаємо рецепти де всі інгредієнти є в наявності
        for recipe in Recipe.objects.all():
            # Отримаємо інгредієнти цього рецепту
            ingredients = recipe.recipe_ingredients.all()
            ingredient_color_ids = [ing.color.id for ing in ingredients]

            # Перевіряємо чи всі ID інгредієнтів є в наявності
            if all(color_id in selected_color_ids for color_id in ingredient_color_ids):
                possible_recipes.append(recipe)

    return render(request, "colors/what_can_i_mix.html", {
        "all_colors": all_colors,
        "selected_colors": selected_colors,
        "possible_recipes": possible_recipes
    })

