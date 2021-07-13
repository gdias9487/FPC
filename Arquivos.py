def mergesort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if end - start > 1:
        mid = (end + start) // 2
        mergesort(array, start, mid)
        mergesort(array, mid, end)
        merge(array, start, mid, end)

    return array


def merge(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    top_left, top_right = 0, 0
    for i in range(start, end):
        if top_left >= len(left):
            array[i] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            array[i] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            array[i] = left[top_left]
            top_left = top_left + 1
        else:
            array[i] = right[top_right]
            top_right = top_right + 1

    return None


def folder(array, n, lenght):
    folders = n
    i, j = 0, n - 1
    while (j > 0) and (i != j) and (i < n - 1):
        if array[i] == 0:
            i += 1

        if array[i] + array[j] > lenght:
            array[j] = 0
            j -= 1

        else:
            if j > i:
                array[i] = array[j] = 0
                folders -= 1
                j -= 1

    return print(folders)


n, byts = [int(x) for x in input().split()]
archives_bytes = mergesort([int(x) for x in input().split()])
folder(archives_bytes, n, byts)
