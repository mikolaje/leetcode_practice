# coding=u8

def binary_search(arr, query):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(mid)
        val = arr[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1

    return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(binary_search(array,3))