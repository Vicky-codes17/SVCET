class Student:
    def __init__(self):
        self.s1 = int(input("Enter the mark1 : "))
        self.s2 = int(input("Enter the mark2 : "))
        self.s3 = int(input("Enter the mark3 : "))
    
    def calculate_percentage(self):
        # total = self.s1+ self.s2 + self.s3
        # res = total // 3
        # return res
        print((self.s1+self.s2+self.s3)//3)

l = []
n = int(input("Enter the number of students : "))
for i in range(n):
    x = Student()
    l.append(x)

for i in range(n):
    l[i].calculate_percentage()