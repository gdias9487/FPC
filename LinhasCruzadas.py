def mergesort(array, start=0, end=None):
    inv = 0
    if end is None:
        end = len(array)
    if end - start > 1:
        mid = (end + start) // 2
        inv = mergesort(array, start, mid) + mergesort(array, mid, end) + merge(array, start, mid, end)

    return inv


def merge(array, start, mid, end):
    inv = 0
    left = array[start:mid]
    right = array[mid:end]
    i = start
    top_left, top_right = 0, 0

    for x in range(start, end):
        if top_left >= len(left):
            array[x] = right[top_right]
            top_right = top_right + 1

        elif top_right >= len(right):
            array[x] = left[top_left]
            top_left = top_left + 1

        elif left[top_left] <= right[top_right]:
            array[x] = left[top_left]
            top_left = top_left + 1

        else:
            array[x] = right[top_right]
            top_right = top_right + 1
            inv += (len(left) - top_left)

    return inv


n = int(input())
nails = [int(x) for x in input().split()]
print(mergesort(nails))
