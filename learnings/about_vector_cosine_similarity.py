import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def vector_cosine_similarity():
    # Features: [Horror Movies Watched, Comedy Movies Watched]
    user_a = np.array([[20, 1]])   # Hardcore Horror fan
    user_b = np.array([[500, 25]]) # Massive movie buff, but same ratio
    user_c = np.array([[5, 25]])   # Comedy fan

    # We compare user_a to the others
    sim_ab = cosine_similarity(user_a, user_b)
    sim_ac = cosine_similarity(user_a, user_c)

    print(f"Similarity (Hardcore vs Massive Buff): {sim_ab[0][0]:.4f}")
    # Result: ~0.999 (The AI sees they have the same taste)

    print(f"Similarity (Hardcore vs Comedy Fan): {sim_ac[0][0]:.4f}")
    # Result: ~0.450 (The AI sees their tastes diverge)

if __name__ == "__main__":
    vector_cosine_similarity()
