import csv

num_attribute=6
print("\n the total number of attributes in dataset are:",num_attribute)
data=[]
print("\n the given training data set \n:")
with open("/home/vignesh/VS/GitHub/SVCET/6th-Semester/Machine_Learning-Lab/Week-1/s_algorithm/data/weather.csv",'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        data.append(row)
        print(row)

hypothesis=['0']*num_attribute
print("\n initial hypothesis is :\n",hypothesis)

for j in range(0,num_attribute):
    hypothesis[j]=data[0][j]

print("\n Find S : Finding a maximally specific hypothesis \n")

for i in range(0,len(data)):
    if data[i][num_attribute]=='yes':
       for j in range(0,num_attribute):
           if data[i][j]!=hypothesis[j]:
               hypothesis[j]='?'
       print("For training instance no:{}, the hypothesis is {}".format(i, hypothesis))
    else:
        continue
print("\n The maximally specific hypothesis for the given training examples is :\n")
print(hypothesis)