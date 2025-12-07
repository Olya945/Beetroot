'''Fibonacci search'''

def fibonacci_search(arr, target):
    n = len(arr)

    # Числа Фібоначчі
    fib2 = 0
    fib1 = 1
    fib = 1

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] == target:
            return i
        
        elif arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1


''' Binary Search (рекурсія) та Fibonacci Search обидва O(log n), але Binary Search простіше'''
