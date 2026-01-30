import pandas as pd
import math

df = pd.read_csv("6th-Semester/Machine_Learning-Lab/Week-3/data.csv")
print("Dataset Loaded Successfully:\n")
print(df)

def entropy(target_col):
    values = target_col.value_counts()
    total = len(target_col)
    ent = 0
    for count in values:
        p = count / total
        ent -= p * math.log2(p)
    return ent

def info_gain(df, feature, target):
    total_entropy = entropy(df[target])
    values = df[feature].unique()
    weighted_entropy = 0
    for v in values:
        subset = df[df[feature] == v]
        weighted_entropy += (len(subset) / len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

def id3(df, features, target):
    if len(df[target].unique()) == 1:
        return df[target].iloc[0]
    if len(features) == 0:
        return df[target].mode()[0]

    gains = {f: info_gain(df, f, target) for f in features}
    best_feature = max(gains, key=gains.get)
    tree = {best_feature: {}}

    for value in df[best_feature].unique():
        subset = df[df[best_feature] == value]
        remaining_features = [f for f in features if f != best_feature]
        tree[best_feature][value] = id3(subset, remaining_features, target)

    return tree

def classify(tree, sample):
    if not isinstance(tree, dict):
        return tree
    root = next(iter(tree))
    value = sample[root]
    if value in tree[root]:
        return classify(tree[root][value], sample)
    else:
        return "Unknown"

features = list(df.columns[:-1])
target = "PlayTennis"

decision_tree = id3(df, features, target)
print("\nGenerated Decision Tree (ID3):\n")
print(decision_tree)

new_sample = {
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "High",
    "Wind": "Strong"
}

result = classify(decision_tree, new_sample)
print("\nNew Sample Classification Result:")
print("Sample =", new_sample)
print("Prediction =", result)
