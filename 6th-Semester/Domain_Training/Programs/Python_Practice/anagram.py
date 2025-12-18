## Check if the two strings are anagrams

# s1 = "listen"
# s2 = "silent"

s1 = input("Enter the first anagram : ")
s2 = input("Enter the second anagram :")

print("Yes" if sorted(s1) == sorted(s2) else "No")