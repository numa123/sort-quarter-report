def quickSort(data, n) -> list:
    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2][3]
        left = [x for x in data if x[3] > pivot]
        middle = [x for x in data if x[3] == pivot]
        right = [x for x in data if x[3] < pivot]
        return quickSort(left, 0) + middle + quickSort(right, 0)
