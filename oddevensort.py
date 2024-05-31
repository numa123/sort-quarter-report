def oddEvenSort(arr, n):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n - 1, 2):
            if arr[i][3] > arr[i + 1][3]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        for i in range(0, n - 1, 2):
            if arr[i][3] > arr[i + 1][3]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

    return arr