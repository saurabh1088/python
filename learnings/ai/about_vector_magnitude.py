import logging
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def vector_magnitude():
    # A 3D vector
    v = np.array([3, 4, 12])

    # Calculate L2 Norm (Euclidean distance from origin)
    magnitude = np.linalg.norm(v)

    print(f"Vector: {v}")
    print(f"Magnitude: {magnitude}")
    # Result: 13.0 (Because sqrt(3^2 + 4^2 + 12^2) = 13)

if __name__ == "__main__":
    vector_magnitude()
