## Remove duplicates from the list
list1 = [10,20,30,10,20,40,50]  
list_without_duplicate = list(set(list1))

# set() is used for the removing the duplication in the list

print(f"Original List with duplication : ",list1)
print(f"List without duplication : ",sorted(list_without_duplicate))
