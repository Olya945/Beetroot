''' Task 3

  One way to improve the quicksort is to use an insertion
sort on lists that are small in length (call it the "partition limit").
Why does this make sense? Re-implement the quicksort and use it to sort 
a random list of integers. Perform analysis using different list sizes
for the partition limit.'''

import random
import time

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i - 1
        nxt_element = arr[i]

        while (arr[j] > nxt_element) and (j >= left):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = nxt_element

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1] 
    
    return i + 1

def quicksort(arr, left, right, partition_limit):
    if left >= right:
        return
    
    size = right - left + 1
    if size <= partition_limit:
        insertion_sort(arr, left, right)
        
    else:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1, partition_limit)
        quicksort(arr, pivot_index + 1, right, partition_limit)

# Тестування
print('=== Тестування Quick Sort з різними partition_limit ===\n')

# Створюємо випадковий масив
test_size = 1000
original = [random.randint(1, 1000) for _ in range(test_size)]

# Тестуємо з різними partition_limit
limits = [5, 10, 15, 20, 30]

for limit in limits:
    arr = original.copy()  # Копіюємо оригінальний масив
    
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1, limit)
    end_time = time.time()
    
    elapsed = (end_time - start_time) * 1000  # Переводимо в мілісекунди
    
    print(f'partition_limit = {limit:2d} → Час: {elapsed:.3f} мс')

# Перевірка правильності
arr_test = [38, 27, 43, 3, 9, 82, 10, 5]
print(f'\nДо сортування: {arr_test}')
quicksort(arr_test, 0, len(arr_test) - 1, 10)
print(f'Після сортування: {arr_test}')
