from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\n--------------------------------------")

correct = []
wrong = []

for i in range(len(y_test)):
    actual = class_names[y_test[i]]
    predicted = class_names[y_pred[i]]
    if y_test[i] == y_pred[i]:
        correct.append((X_test[i], actual, predicted))
    else:
        wrong.append((X_test[i], actual, predicted))

print("\n Correct Predictions:")
for features, actual, predicted in correct[:5]:
    print(f"Input: {features} | Actual: {actual} | Predicted: {predicted}")

print("\n Wrong Predictions:")
for features, actual, predicted in wrong[:5]:
    print(f"Input: {features} | Actual: {actual} | Predicted: {predicted}")

print("\n--------------------------------------")
print("Total Correct:", len(correct))
print("Total Wrong:", len(wrong))
