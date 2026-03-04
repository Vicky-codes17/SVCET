import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("6th-Semester/Machine_Learning-Lab/Week-5/sample.csv")
X = data.iloc[:, :-1]   
y = data.iloc[:, -1]    
encoder = LabelEncoder()

for column in X.columns:
    X[column] = encoder.fit_transform(X[column])
y = encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Predicted values:", y_pred)
print("Actual values:", y_test)
print("Accuracy:", accuracy * 100, "%")
print("\nDetailed Results:")
for i in range(len(y_test)):
    print("Predicted:", y_pred[i], " | Actual:", y_test[i])