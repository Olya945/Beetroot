''' Task 2

Implement the mergeSort function without using the slice operator.'''

def merge(arr, left, mid, right):
    
    # Розмір лівої частини
    left_size = mid - left + 1

    # Розмір правої частини  
    right_size = right - mid

    # Створюємо порожні списки
    left_arr = []
    right_arr = []

    # Копіюємо ліву частину
    for i in range(left_size):
        left_arr.append(arr[left + i])
    
    # Копіюємо праву частину
    for i in range(right_size):
        right_arr.append(arr[mid + 1 + i])
    
    i = 0
    j = 0
    k = left

    # Зливаємо праву і ліву частину
    while i < left_size and j < right_size:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Додаємо елементи лівої частини списку, якщо вони залишились
    while i < left_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Додаємо елементи правої частини списку, якщо вони залишились
    while j < right_size:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left >= right:
        return
    
    mid = (left + right) // 2
    
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)

arr = [38, 27, 43, 3, 9, 82, 10, 5]
print('До сортування: ', arr)
mergeSort(arr, 0, len(arr) - 1)
print('Після сортування: ', arr)