a = [[12,33,44,14,
      55,36,37,38,
      66,67,68,69,
      32,11,43,12]]

row = len(a)
col = len(a[0])
top = 0
left = 0
right = row-1
bottom = col-1

while(left<=right and top<=bottom):
    for i in range(left,right + 1):
        print(a[top][i], end = " ")
    top = top + 1

    for i in range(top, bottom +1):
        print(a[left][i], end = " ")
    right = right - 1

    for i in range(right, left -1, -1):
        print(a[bottom][i], end = " ")
    bottom = bottom - 1

    for i in range(bottom, top -1, -1):
        print(a[left][i], end = " ")
    left = left + 1
        