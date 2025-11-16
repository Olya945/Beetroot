def binary_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        mid2 = (low + high) // 2
        print(mid, mid2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = [x for x in range(1000)]
x = 500

result = binary_search(arr, 10, len(arr) - 1, x)