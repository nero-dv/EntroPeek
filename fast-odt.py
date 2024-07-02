import numpy as np
from collections import Counter
from math import log2


def entropy(attribute_values):
    """Calculate the entropy of a list of attribute values."""
    n = len(attribute_values)
    count = Counter(attribute_values)
    probabilities = [count[val] / n for val in count]
    return -sum(p * log2(p) for p in probabilities)


def entropy_difference(data, i, j):
    """Calculate the entropy difference for attribute value X_{i,j}."""
    X_i = data[:, i]
    X_i_j_removed = np.delete(data[:, i], j)
    return entropy(X_i) - entropy(X_i_j_removed)


def calculate_threshold_alpha(data):
    """Calculate the threshold alpha for entropy difference."""
    m, n = data.shape
    sum_entropy_diff = 0
    count_positive_diff = 0

    for i in range(n):  # Iterate over columns
        for j in range(m):  # Iterate over rows in the current column
            diff = entropy_difference(data, i, j)
            if diff > 0:
                sum_entropy_diff += diff
                count_positive_diff += 1

    return sum_entropy_diff / count_positive_diff if count_positive_diff > 0 else 0


def detect_outliers(data, alpha):
    """Detect outliers based on the entropy difference threshold alpha."""
    m, n = data.shape
    outliers = []

    for i in range(n):  # Iterate over columns
        for j in range(m):  # Iterate over rows in the current column
            diff = entropy_difference(data, i, j)
            if diff > alpha:
                outliers.append((i, j))

    return outliers


# Example usage
if __name__ == "__main__":
    # Sample data
    data = np.array(
        [
            # 0  1  2
            [1, 2, 3], #0
            [1, 2, 3], #1
            [4, 5, 6], #2
            [1, 2, 3], #...
            [4, 5, 6],
            [7, 8, 9],
            [1, 5, 9],
            [4, 2, 6],
            [4, 2, 6],
            [1, 5, 9],
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 5, 9],
            [4, 2, 6],
            [4, 2, 6],
            [1, 5, 9],
        ]
    )

    # Calculate alpha
    alpha = calculate_threshold_alpha(data)
    print(f"Calculated Threshold Alpha: {alpha}")

    # Detect outliers
    outliers = detect_outliers(data, alpha)
    print(f"Detected Outliers: {outliers}")
