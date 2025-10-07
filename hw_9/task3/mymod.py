"""Функція виконує підрахунок
кількості рядків у тексті"""

def count_lines(name):
    file = open(name, 'r')
    lines = file.readlines()
    file.close()
    return len(lines)


"""Функція виконує підрахунок
кількості символів у файлі"""

def count_chars(name):
    file = open(name, 'r')
    text = file.read()
    return len(text)


"""Функція тестує дві
попередні функції"""
def test(name):
    lines = count_lines(name)
    chars = count_chars(name)

    print(f'File: {name}')
    print(f'Number of lines: {lines}')
    print(f'Number of chars: {chars}')
