from django.contrib import admin
from .models import Color, Recipe, RecipeIngredient

# Реєструє модель Color в admin панелі
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    # Які колонки показувати в списку
    list_display = ["name", "code", "is_primary"] 

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 2  # Показати 2 порожні рядки для інгредієнтів
    fields = ["color", "order"]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["result", "proportions", "created_at"]
    inlines = [RecipeIngredientInline]
