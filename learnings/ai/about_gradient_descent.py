"""
Gradient Descent Implementation and Concept Exploration.

This module demonstrates the gradient descent optimization algorithm, a fundamental
technique in machine learning used to minimize loss functions and train predictive
models. It provides a hands-on implementation of linear regression using gradient
descent with synthetic data.

Concept Overview:
    Gradient Descent is an iterative optimization algorithm that adjusts model
    parameters to minimize a loss function. The algorithm works by:
    
    1. Computing predictions using current parameters
    2. Calculating the loss (error) between predictions and actual values
    3. Computing gradients (partial derivatives) of the loss with respect to each parameter
    4. Updating parameters in the direction opposite to the gradient
    5. Repeating until convergence (when loss stops decreasing significantly)
    
    The key insight is that gradients point in the direction of steepest increase,
    so moving opposite to the gradient reduces the loss.

Approach Used:
    - Linear Regression: Learn a linear relationship y = wx + b
    - Mean Squared Error (MSE): Loss function measuring prediction accuracy
    - Batch Gradient Descent: Update parameters using all data points per iteration
    - Manual differentiation: Explicit gradient computation for w and b

APIs and Dependencies:
    numpy (np): For efficient numerical computations on arrays
        - np.array(): Create numpy arrays from Python lists
        - np.mean(): Compute mean value across array elements
        - np.sum(): Sum all array elements
        - Array operations: Element-wise multiplication and arithmetic

Mathematical Formulation:
    Model: y_pred = w*X + b
    
    Loss: L = (1/n) * Σ(y_pred - y)²
    
    Gradients:
        dL/dw = (2/n) * Σ(X * (y_pred - y))
        dL/db = (2/n) * Σ(y_pred - y)
    
    Updates (with learning rate α):
        w_new = w_old - α * dL/dw
        b_new = b_old - α * dL/db

Example:
    Target: Learn the linear function y = 3x + 2
    
    The algorithm successfully discovers w ≈ 3.0 and b ≈ 2.0 through iterative
    optimization over 1000 epochs.
"""

import numpy as np


def gradient_descent_example():
    """
    Execute gradient descent optimization on synthetic linear regression data.
    
    This function demonstrates the complete gradient descent workflow:
    - Creates synthetic training data following y = 3x + 2
    - Initializes model parameters randomly
    - Iteratively improves parameters by following negative gradients
    - Reports progress at regular intervals
    - Prints final learned parameters
    
    Returns:
        tuple: A tuple containing (final_weight, final_bias, history_losses)
            - final_weight (float): Learned slope parameter
            - final_bias (float): Learned intercept parameter
            - Note: Losses are printed but not returned in this implementation
    
    Hyperparameters:
        learning_rate (float): Controls step size during parameter updates.
                               Too high causes instability; too low causes slow convergence.
        epochs (int): Number of complete passes through the training data.
    """
    # =====================================================================
    # 1. DATA PREPARATION
    # =====================================================================
    # Create synthetic training data following the relationship: y = 3x + 2
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 8, 11, 14, 17])  # Each value follows: y = 3*x + 2
    
    # =====================================================================
    # 2. PARAMETER INITIALIZATION
    # =====================================================================
    # Initialize model parameters to small random values
    w = 0.0  # Weight/Slope: Multiplier for X
    b = 0.0  # Bias/Intercept: Constant offset
    
    # Hyperparameters
    learning_rate = 0.01  # Controls magnitude of parameter updates
    epochs = 1000         # Number of training iterations
    n_samples = len(X)    # Total number of training examples
    
    # =====================================================================
    # 3. TRAINING LOOP: ITERATIVE OPTIMIZATION
    # =====================================================================
    for epoch in range(epochs):
        # -------------------------------------------
        # Step 1: Forward Pass - Make Predictions
        # -------------------------------------------
        # Compute model predictions using current parameters
        y_pred = w * X + b
        
        # -------------------------------------------
        # Step 2: Calculate Loss (MSE)
        # -------------------------------------------
        # Mean Squared Error: Average of squared prediction errors
        # This quantifies how well the model fits the data
        loss = np.mean((y_pred - y)**2)
        
        # -------------------------------------------
        # Step 3: Backpropagation - Compute Gradients
        # -------------------------------------------
        # Gradients indicate how much each parameter contributes to the loss
        # We compute partial derivatives using the chain rule
        
        # Gradient w.r.t. weight (w):
        # dL/dw = (2/n) * Σ[X_i * (y_pred_i - y_i)]
        # Measures sensitivity of loss to changes in weight
        dw = (2 / n_samples) * np.sum(X * (y_pred - y))
        
        # Gradient w.r.t. bias (b):
        # dL/db = (2/n) * Σ[(y_pred_i - y_i)]
        # Measures sensitivity of loss to changes in bias
        db = (2 / n_samples) * np.sum(y_pred - y)
        
        # -------------------------------------------
        # Step 4: Parameter Update (Gradient Descent)
        # -------------------------------------------
        # Move parameters opposite to the gradient direction
        # This descends the loss surface toward lower error
        w = w - (learning_rate * dw)
        b = b - (learning_rate * db)
        
        # -------------------------------------------
        # Step 5: Logging Progress
        # -------------------------------------------
        if epoch % 100 == 0:
            print(f"Epoch {epoch:4d}: Loss = {loss:.6f}, w = {w:.4f}, b = {b:.4f}")
    
    # =====================================================================
    # 4. RESULTS
    # =====================================================================
    print(f"\n{'='*65}")
    print(f"Training Complete!")
    print(f"{'='*65}")
    print(f"Final Parameters:")
    print(f"  Weight (Slope):     w = {w:.4f}  (Target: 3.0)")
    print(f"  Bias (Intercept):   b = {b:.4f}  (Target: 2.0)")
    print(f"{'='*65}")
    print(f"\nLearned Model: y = {w:.2f}x + {b:.2f}")
    print(f"Expected Model: y = 3.00x + 2.00")
    
    return w, b


# =====================================================================
# MODULE EXECUTION
# =====================================================================
if __name__ == "__main__":
    """Execute the gradient descent example when run as a script."""
    final_w, final_b = gradient_descent_example()

