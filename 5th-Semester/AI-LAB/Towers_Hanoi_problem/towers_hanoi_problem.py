### Write a program to implement Towers of Hanoi problem.

def towers_of_hanoi(n,source,auxiliary,destination):
    if n==1:
        print("Move disk 1 from",source,"to",destination)
        return
    towers_of_hanoi(n-1,source,destination,auxiliary)
    print("Move disk",n,"from",source,"to",destination)
    towers_of_hanoi(n-1,auxiliary,source,destination)

n = 3
towers_of_hanoi(n,'A','B','C')