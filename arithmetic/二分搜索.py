def binary_search(array, t):
    low = 0
    height = len(array) - 1
    while low < height:
        mid = (low + height) / 2
        if array[mid] < t:
            low = mid + 1

        elif array[mid] > t:
            height = mid - 1

        else:
            return array[mid]

    return -1
