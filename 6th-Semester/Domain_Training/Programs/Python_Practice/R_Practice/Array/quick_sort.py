def QS(arr):
    if (len(arr) <=1):
        return arr
    pivot = arr[0]
    left = []
    right = []

    for i in range(1,len(arr)):
        if (arr[i]<pivot):
            left.append(arr[i])
        else:
            right.append(arr[i])
    return QS(left)+[pivot]+QS(right)

arr = [2,55,3,45,12,66,10,13,44,11,22]
result = QS(arr)
print(result)