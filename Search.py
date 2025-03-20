def binarySearch(arr, target):
    lower = 0
    upper = len(arr) - 1
    found = False
    while lower <= upper and not found:
        mid = (lower + upper) // 2
        if target < arr[mid]:
            upper = mid - 1
        elif target > arr[mid]:
            lower = mid + 1
        else:
            found = True
    if found:
        print(target, "is found")
    else:
        print("Not found.")
data = [2, 6, 13, 16, 23, 25, 37, 40, 49, 55]
binarySearch(data, 3)
