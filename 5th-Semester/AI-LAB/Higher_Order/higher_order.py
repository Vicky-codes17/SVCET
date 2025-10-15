### Counting Strings in a List using Higher-Order Functions

def count(test, lst):
    result = 0
    for item in lst:
        if test(item):
            result += 1
    return result

print(count(lambda x: x > 2, [1, 2, 3, 4, 5]))  # Output: 3