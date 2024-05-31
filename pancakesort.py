def flip(arr, k):
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        k -= 1
        left += 1

def max_index(arr, k):
    index = 0
    for i in range(1, k + 1):
        if arr[i][3] > arr[index][3]:
            index = i
    return index

def pancakeSort(arr, n):
    while n > 1:
        maxdex = max_index(arr, n - 1)
        if maxdex != n - 1:
            flip(arr, maxdex)
            flip(arr, n - 1)
        n -= 1
    return arr