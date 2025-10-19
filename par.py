from functools import partial

def multiply(a, b, c, d):
    return a * b * c * d

multiply_by_2_and_3 = partial(multiply, 2, 3)
result = multiply_by_2_and_3(4, 5)  # This will compute 2 * 3 * 4 * 5
print(result)

multiply(2, 3, 4, 5)