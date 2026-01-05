class Color:
    """Клас для представлення кольору"""

    def __init__(self, name, is_primary=False):
        self.name = name
        self.is_primary = is_primary #Базовий колір

        pass

    def __str__(self):

        return f"Color: {self.name}"

    def __repr__(self):

        return f"Color('{self.name}', {self.is_primary})"
    