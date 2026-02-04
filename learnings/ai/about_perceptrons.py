import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        # Initialize weights randomly and bias to 0
        self.weights = np.random.randn(input_size)
        self.bias = 0
        self.lr = learning_rate
        print(f"Initialized weights: {self.weights}, bias: {self.bias}")

    def activation(self, x):
        # The Step Function (Binary output)
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        # Calculation: (Inputs * Weights) + Bias
        linear_output = np.dot(inputs, self.weights) + self.bias
        return self.activation(linear_output)

    def train(self, training_data, labels, epochs=100):
        for _ in range(epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                # Error = Desired Output - Predicted Output
                error = label - prediction
                # Update weights and bias based on error
                self.weights += self.lr * error * inputs
                self.bias += self.lr * error

# --- Testing the Perceptron ---
# AND Gate Data
if __name__ == "__main__":
    inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
    labels = np.array([0, 0, 0, 1])

    perceptron = Perceptron(input_size=2)
    perceptron.train(inputs, labels)

    print("Trained weights:", perceptron.weights)
    print("Trained bias:", perceptron.bias)

    # Predict
    print(f"Prediction for [1, 1]: {perceptron.predict(np.array([1, 1]))}") # Should be 1
    print(f"Prediction for [0, 1]: {perceptron.predict(np.array([0, 1]))}") # Should be 0
