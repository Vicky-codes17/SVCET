## Find the second largest number in the list
list1 = [23,12,55,88,22,14]
list1.sort(reverse= True)  # 88, 55, 23, 22, 14, 12
print(list1[1])

# Smallest number in list
list1.sort(reverse=False)
print(list1[0])