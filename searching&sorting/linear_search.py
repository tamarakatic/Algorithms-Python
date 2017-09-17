def linear_search(arr, x):
    res = -1
    for i in range(len(arr)):
        if arr[i] == x : res = i
    return res
