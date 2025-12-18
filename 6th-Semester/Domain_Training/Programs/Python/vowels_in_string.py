## Given a string count the number of vowels
string1 = "hello"
v = 'aeiouAEIOU'
res = 0
for c in string1:
    if c in v:
        res +=1
print(res)

        