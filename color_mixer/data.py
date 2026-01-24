"""База даних змішування кольорів"""

# ============== КОНСТАНТИ КОЛЬОРІВ ==============

# Первинні кольори
RED = "червоний"
BLUE = "синій"
YELLOW = "жовтий"
WHITE = "білий"
BLACK = "чорний"

# Вторинні кольори
ORANGE = "помаранчевий"
GREEN = "зелений"
PURPLE = "фіолетовий"

# Відтінки
PINK = "рожевий"
LIGHT_BLUE = "блакитний"
MINT = "м'ятний"
LAVENDER = "лавандовий"
PEACH = "персиковий"
TURQUOISE = "бірюзовий"

# Складні кольори
BROWN = "коричневий"
DARK_BROWN = "темно-коричневий"
OLIVE = "оливковий"
TERRACOTTA = "теракотовий"
GRAY = "сірий"
WARM_GRAY = "теплий сірий"

# ============== РЕЦЕПТИ ==============
RECIPES = [
    {
        "result": ORANGE,
        "ingredients": [YELLOW, RED],
        "proportions": "1:1"
    },
    {
        "result": GREEN,
        "ingredients": [YELLOW, BLUE],
        "proportions": "1:1"
    },
    {
        "result": PURPLE,
        "ingredients": [BLUE, RED],
        "proportions": "1:1"
    },
    {
        "result": PINK,
        "ingredients": [RED, WHITE],
        "proportions": "1:3"
    },
    {
        "result": LIGHT_BLUE,
        "ingredients": [BLUE, WHITE],
        "proportions": "1:2"
    },
    {
        "result": MINT,
        "ingredients": [GREEN, WHITE],
        "proportions": "1:1"
    },
    {
        "result": LAVENDER,
        "ingredients": [PURPLE, WHITE],
        "proportions": "1:1"
    },
    {
        "result": PEACH,
        "ingredients": [ORANGE, WHITE],
        "proportions": "1:1"
    },
    {
        "result": TURQUOISE,
        "ingredients": [BLUE, GREEN],
        "proportions": "1:1"
    },
    {
        "result": BROWN,
        "ingredients": [RED, GREEN],
        "proportions": "1:1"
    },
    {
        "result": DARK_BROWN,
        "ingredients": [PURPLE, YELLOW],
        "proportions": "1:1"
    },
    {
        "result": OLIVE,
        "ingredients": [GREEN, YELLOW],
        "proportions": "2:1"
    },
    {
        "result": TERRACOTTA,
        "ingredients": [BROWN, ORANGE],
        "proportions": "1:1"
    },
    {
        "result": GRAY,
        "ingredients": [BLACK, WHITE],
        "proportions": "1:1"
    },
    {
        "result": WARM_GRAY,
        "ingredients": [YELLOW, PURPLE],
        "proportions": "1:2"
    },
    {
        "result": BLACK,
        "ingredients": [RED, BLUE, YELLOW],
        "proportions": "1:1:1"
    },
    {
        "result": BLACK,
        "ingredients": [BROWN, BLUE],
        "proportions": "2:1"
    },
    {
        "result": BLACK,
        "ingredients": [PURPLE, BROWN],
        "proportions": "1:1"
    }
]

PRIMARY_COLORS = [RED, BLUE, YELLOW, WHITE]