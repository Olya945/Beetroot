"""Клас для логіки змішування кольорів"""

from recipe import Recipe
from data import RECIPES, PRIMARY_COLORS

class ColorMixer:
    """Міксер кольорів - знаходить рецепти змішування"""

    def __init__(self):
        self.recipes = []

        for recipe_dict in RECIPES:
            recipe_obj = Recipe(
                result=recipe_dict["result"],
                ingredients=recipe_dict["ingredients"],
                proportions=recipe_dict["proportions"]
            )
            self.recipes.append(recipe_obj)

    def find_recipe(self, color_name):
        """Знаходить рецепт для заданого кольору"""

        # Перевіряємо чи колір є первинним
        if self.is_primary(color_name):
            return None
        
        # Шукаємо рецепти
        found_recipes = []

        for recipe in self.recipes:
            if recipe.result == color_name:
                found_recipes.append(recipe)
        
        # Повертаємо результат
        if not found_recipes:
            return None
        else: 
            return found_recipes
    
     

    def is_primary(self, color_name):
        """Перевіряє чи є колір первинним"""
        
        return color_name in PRIMARY_COLORS

