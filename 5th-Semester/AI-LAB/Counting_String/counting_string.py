### Counting the number of times a substring appears in a string using recursion

def countsubstring(s1, s2):
    if len(s2) < len(s1):
        return 0
    if s2[:len(s1)] == s1:
        return 1 + countsubstring(s1, s2[1:])  
    else:
        return countsubstring(s1, s2[1:])       

print(countsubstring('ab', 'cabalaba')) 