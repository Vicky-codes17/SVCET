import pandas as pd
d = {"Name":["Vignesh","Viki","Ramesh"],
     "Age":[21,22,20],
     "Marks":[88,77,88]
     }
x = pd.DataFrame(d)
print(x)

# Filtering
print(x[x["Age"] > 20])