import numpy as np

# ----------------------------------------------------------
# Gradient Descent Implementation

# The Goal: Learn y = 3x + 2
# Create a dataset where y is always three times x plus two. 

# Create synthetic data
X = np.array([1, 2, 3, 4, 5])
y = np.array([5, 8, 11, 14, 17]) # Follows y = 3x + 2

# Initialize parameters
w = 0.0  # Weight (Slope)
b = 0.0  # Bias (Intercept)
learning_rate = 0.01
epochs = 1000

# 3. The Training Loop
for epoch in range(epochs):
    # --- Forward Pass ---
    y_pred = w * X + b
    
    # --- Calculate Loss (Mean Squared Error) ---
    loss = np.mean((y_pred - y)**2)
    
    # --- Backpropagation (Calculating Gradients) ---
    # How much does 'w' and 'b' contribute to the error?
    dw = (2/len(X)) * np.sum(X * (y_pred - y))
    db = (2/len(X)) * np.sum(y_pred - y)
    
    # --- Gradient Descent (The Update) ---
    w = w - (learning_rate * dw)
    b = b - (learning_rate * db)
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.4f}, w = {w:.2f}, b = {b:.2f}")

print(f"\nFinal Result: y = {w:.2f}x + {b:.2f}")

