import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from sklearn.preprocessing import KBinsDiscretizer

data = pd.read_csv("6th-Semester/Machine_Learning-Lab/Week-7/heart.csv")

features = ['age','chol','thalach','trestbps']
target = 'target'

disc = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
data[features] = disc.fit_transform(data[features])

data = data.astype(int)

model = DiscreteBayesianNetwork([
    ('age','target'),
    ('chol','target'),
    ('thalach','target'),
    ('trestbps','target'),
    ('cp','target'),
    ('exang','target')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

result = infer.query(
    variables=['target'],
    evidence={
        'age':1,
        'chol':1,
        'thalach':2,
        'trestbps':1,
        'cp':1,
        'exang':0
    }
)

print(result)