class Result:
    name = "Vignesh"
    def show(self):
        print("Hi")
    def display(self):
        print(Result.name)
        self.x = int(input("Enter a number : "))
    def printer(self):
        print(self.x)

s1 = Result()
s1.show()
s1.display()
s1.printer()

# a = Result()
# b = Result()

# a.display()
# b.display()

