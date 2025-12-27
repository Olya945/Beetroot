''' Task 1

A bubble sort can be modified to "bubble" in both directions.
The first pass moves "up" the list and the second pass moves
"down." This alternating pattern continues until no more passes
are necessary. Implement this variation and describe under what
circumstances it might be appropriate.'''


def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False

        # Перямий прохід
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        # Зворотний прохід
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True


    return arr

# Тест
numbers = [5, 1, 4, 2, 8, 0, 2]
print(cocktail_sort(numbers))

''' Цей масив може бути доречним коли малі числа стоять в кінці списку
або велики числа стоять на початку списку, або масив має зворотній порядок чисел'''