''' Реалізація алгоритму бінарного пошуку за допомогою рекурсії '''

def binary_search_recursive(arr, num, left, right):
   
    if left > right:
        return -1
    
    mid = (right + left)//2

    if arr[mid] == num:
        return mid
    
    elif arr[mid] > num:
        return binary_search_recursive(arr, num, left, mid - 1)
   
    elif arr[mid] < num:
        return binary_search_recursive(arr, num, mid + 1, right)
    

