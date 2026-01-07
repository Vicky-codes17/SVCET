# Income Tax of 10%
class Tax:
    rate = int(input("Enter the rate : "))
    def cal_value(self):
        self.sal = int(input("Enter the salary : "))
        print(self.sal * Tax.rate/100)

a = Tax()
b = Tax()
c = Tax()

a.cal_value()
b.cal_value()
c.cal_value()