def binarysearch(vals, value):
    lo = 0
    hi = len(vals) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if vals[mid] < value:
            lo = mid + 1
        elif value < vals[mid]:
            hi = mid - 1
        else:
            return mid
    return None
 