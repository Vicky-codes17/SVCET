class Result():
    name = "Vignesh"
    def show(self):
        print("Hello")
    def display(self):
        print(Result.name)
        self.x = int(input("Enter the number : "))
    def printer(self):
        print(self.x)

s1 = Result()
s2 = Result()

s1.show()
s2.show()

s1.display()
s2.display()

s1.printer()
s2.printer()