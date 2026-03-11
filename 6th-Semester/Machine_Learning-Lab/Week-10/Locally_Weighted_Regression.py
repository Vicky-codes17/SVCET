import numpy as np
import matplotlib.pyplot as plt

def kernel(x, X, tau):
    m = X.shape[0]
    weights = np.eye(m)
    for i in range(m):
        diff = x - X[i]
        weights[i,i] = np.exp(-(diff @ diff.T) / (2 * tau**2))

    return weights

def locally_weighted_regression(x_query, X, y, tau):
    W = kernel(x_query, X, tau)
    XTX = X.T @ W @ X
    theta = np.linalg.pinv(XTX) @ X.T @ W @ y
    return x_query @ theta
x = np.linspace(-3,3,50)
y = np.sin(x) + np.random.normal(0,0.1,50)

X = np.vstack((np.ones(len(x)), x)).T

tau = 0.5
y_pred = []
for i in range(len(x)):
    y_pred.append(locally_weighted_regression(X[i], X, y, tau))
y_pred = np.array(y_pred)
plt.scatter(x, y, color="red", label="Original Data")
plt.plot(x, y_pred, color="blue", label="LWR Fit")
plt.title("Locally Weighted Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()