def selectionSort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx][3] > arr[j][3]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
