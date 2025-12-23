# Find S Algorithm
import pandas as pd

data = pd.DataFrame({
    'Color': ['Red', 'Red', 'Green', 'Green', 'Red'],
    'Texture': ['Smooth', 'Rough', 'Smooth', 'Rough', 'Smooth'],
    'Label': ['Positive', 'Positive', 'Negative', 'Negative', 'Positive']
})

hypothesis = ['None'] * (data.shape[1] - 1)


for i in range(len(data)):
    if data.iloc[i]['Label'] == 'Positive':
        for j in range(len(hypothesis)):
            if hypothesis[j] == 'None':
                hypothesis[j] = data.iloc[i][j]
            elif hypothesis[j] != data.iloc[i][j]:
                hypothesis[j] = '?'
print("Final Hypothesis:", hypothesis)