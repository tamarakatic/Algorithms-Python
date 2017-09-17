def binary_search(arr, first, last, x):
    res = -1;
    if last >= first:
        while first <= last:
            half = (first + last) // 2
            if arr[half] == x:
                res = half
                return res
            elif x > arr[half]:
                first = half + 1
            else:
                last = half - 1
        return res
    else:
        return res
