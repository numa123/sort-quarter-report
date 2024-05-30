def partition(array, start, end):
    pivot = array[start][3]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high][3] >= pivot:
            high = high - 1

        while low <= high and array[low][3] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quickSort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)
    return array
