from django.db import models
from colorfield.fields import ColorField

class Color(models.Model):
    """Модель кольору"""

    name = models.CharField(max_length=50, unique=True, verbose_name="Назва")
    code = models.CharField(max_length=20, unique=True, verbose_name="Код")
    is_primary = models.BooleanField(default=False, verbose_name="Первинний")
    color = ColorField(default='#FFFFFF', verbose_name="Колір НЕХ")

    class Meta:
        verbose_name = "Колір"
        verbose_name_plural = "Кольори"
        ordering = ['name']
    
    def is_primary_color(self):
        """Перевіряє чи колір первинний"""
        return self.is_primary
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    """Модель для рецепту змішування"""
    result = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Результат"
    )
    proportions = models.CharField(max_length=20, verbose_name="Пропорції", default="1:1")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепти"
    
    def __str__(self):
        ingredients = " + ".join([ing.color.name for ing in self.recipe_ingredients.all()])
        return f"{self.result.name} = {ingredients} ({self.proportions})"
    
class RecipeIngredient(models.Model):
    """Інгредієнт рецепту"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients",
        verbose_name="Рецепт"
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name="Колір-інгрієнт"
    )
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Інгредієнт"
        verbose_name_plural = "Інгредієнти"
        ordering = ["order"]

    def __str__(self):
        return f"{self.recipe.result.name}: {self.color.name}"