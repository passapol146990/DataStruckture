def bubbleSort(arr):
    for i in range(len(arr)-1):
        isSwappen = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp  = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                isSwappen = False
        if isSwappen:break
    return arr