import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.w1 = np.random.rand(input_nodes, hidden_nodes)
        self.w2 = np.random.rand(hidden_nodes, output_nodes)
        self.lr = 0.5
    def forward(self, X):
        self.hidden_input = np.dot(X, self.w1)
        self.hidden_output = sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.w2)
        self.output = sigmoid(self.final_input)
        return self.output
    def backward(self, X, y):
        error = y - self.output
        d_output = error * sigmoid_derivative(self.output)
        hidden_error = np.dot(d_output, self.w2.T)
        d_hidden = hidden_error * sigmoid_derivative(self.hidden_output)
        self.w2 += np.dot(self.hidden_output.T, d_output) * self.lr
        self.w1 += np.dot(X.T, d_hidden) * self.lr
    def train(self, X, y, epochs):
        for i in range(epochs):
            self.forward(X)
            self.backward(X, y)
            if i % 1000 == 0:
                loss = np.mean((y - self.output)**2)
                print("Epoch:", i, "Loss:", loss)
X = np.array([
[0,0],
[0,1],
[1,0],
[1,1]
])
y = np.array([
[0],
[1],
[1],
[0]
])
nn = NeuralNetwork(2,4,1)
nn.train(X,y,10000)
print("\nFinal Predictions")
predictions = nn.forward(X)
for i in range(len(X)):
    print("Input:",X[i],"Output:",predictions[i])