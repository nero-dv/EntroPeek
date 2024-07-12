# EntroPeek
EntropyPeek is an unofficial implementation of [Fast-ODT (Fast Outlier Detection Tree)](https://ieeexplore.ieee.org/document/9189844). This python project calculates the entropy of attribute values in a dataset and identifies outliers based on an entropy difference threshold.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Limitations](#limitations)

## Features
- Calculate entropy of attribute values.
- Compute entropy difference when an attribute value is removed.
- Determine threshold alpha for entropy differences.
- Detect outliers in the dataset based on the alpha threshold.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nero-dv/EntroPeek.git
    ```
2. **Navigate into the project directory**:
    ```bash
    cd EntroPeek
    ```
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Import the necessary modules and classes**:
    ```python
    import numpy as np
    from fast-odt import calculate_threshold_alpha, detect_outliers
    ```

2. **Initialize the analyzer with your data**:
    ```python
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
    ```

3. **Calculate alpha and detect outliers**:
    ```python
    # Calculate alpha
    alpha = calculate_threshold_alpha(data)
    print(f"Calculated Threshold Alpha: {alpha}")

    # Detect outliers
    outliers = detect_outliers(data, alpha)
    print(f"Detected Outliers: {outliers}")
    ```



## Limitations

The FastODT (Fast Entropy-based Outlier Detection Technique) algorithm has several limitations that should be considered when applying it to different types of datasets.

#### 1. Feature Representation Sensitivity
- Attribute Dependency: The algorithm’s effectiveness is highly dependent on the feature representation of the dataset. If the chosen features do not capture the underlying patterns well, the algorithm might not effectively detect outliers.
- Image Data: Direct application to high-dimensional data like images can be challenging without appropriate feature extraction and dimensionality reduction techniques.
#### 2. Scalability Issues
- High-Dimensional Data: For datasets with a very large number of attributes (features), the computation of entropy differences can become computationally intensive.
- Large Datasets: The algorithm’s performance might degrade as the dataset size grows significantly, both in terms of the number of objects and attributes.
#### 3. Entropy Calculation Assumptions
- Entropy Difference: The algorithm assumes that the difference in entropy after removing a value is a sufficient indicator of an outlier. This might not always be true for datasets with complex distributions.
- Data Distribution: Assumptions about the data distribution might not hold in practical scenarios, affecting the accuracy and reliability of the outlier detection.
#### 4. Parameter Sensitivity
- Threshold (α): The choice of the threshold (α) is crucial. While a heuristic is provided, it might not be universally optimal for all datasets. Misestimation can lead to either an excess of false positives (normal data marked as outliers) or misses (true outliers not detected).
#### 5. Handling of Ties and Zero Differences
- Zero or Exact Matches: The algorithm might not handle cases where entropy differences are zero or multiple attributes/values have the same entropy. This could lead to arbitrary or inconsistent detections.
- Dominant Values: In cases where a few values dominate the dataset, the algorithm might fail to detect subtle outliers among the dominant values.
#### 6. No Temporal or Sequential Analysis
- Static Analysis: FastODT is designed for static datasets and does not account for temporal or sequential dependencies. For time-series or sequential data, temporal outliers might be missed.
#### 7. Interpretability Challenges
- Complexity: Understanding and interpreting why a specific value is marked as an outlier based on entropy differences can be less intuitive compared to other methods like distance-based or density-based outlier detection.
#### 8. Non-robustness to Noise
- Noise Sensitivity: Entropy-based methods can be sensitive to noise, especially if the noise significantly alters the entropy of the dataset. This might lead to unreliable outlier detection in noisy datasets.
#### 9. Application-Specific Limitations
- Domain Constraints: Certain domains might have specific constraints or requirements that FastODT does not address directly. Customization might be needed to tailor the algorithm to specific use cases.
