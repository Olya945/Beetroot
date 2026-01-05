class Recipe:
    """Клас для рецепту змішування кольорів"""

    def __init__(self, result, ingredients, proportions="1:1"):
        self.result = result
        self.ingredients = ingredients
        self.proportions = proportions

        pass

    def __str__(self):

        ingredients_str = " + ".join(self.ingredients)

        return f"{self.result.capitalize()} = {ingredients_str} ({self.proportions})"