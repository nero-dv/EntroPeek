# EntroPeek
EntropyPeek is an unofficial implementation of [Fast-ODT (Fast Outlier Detection Tree)](https://ieeexplore.ieee.org/document/9189844). This python project calculates the entropy of attribute values in a dataset and identifies outliers based on an entropy difference threshold.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Features
- Calculate entropy of attribute values.
- Compute entropy difference when an attribute value is removed.
- Determine threshold alpha for entropy differences.
- Detect outliers in the dataset based on the alpha threshold.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/entropy-analyzer.git
    ```
2. **Navigate into the project directory**:
    ```bash
    cd entropy-analyzer
    ```
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Import the necessary modules and classes**:
    ```python
    import numpy as np
    from entropy_analyzer import EntropyAnalyzer
    ```

2. **Initialize the EntropyAnalyzer with your data**:
    ```python
    data = np.array([
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
    ])

    analyzer = EntropyAnalyzer(data)
    ```

3. **Calculate alpha and detect outliers**:
    ```python
    alpha = analyzer.calculate_threshold_alpha()
    outliers = analyzer.detect_outliers(alpha)
    print(f"Calculated Threshold Alpha: {alpha}")
    print(f"Detected Outliers: {outliers}")
    ```

## Example

Here is an example demonstrating how to use the Entropy Analyzer:

```python
import numpy as np
from entropy_analyzer import EntropyAnalyzer

data = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

analyzer = EntropyAnalyzer(data)

# Calculate alpha
alpha = analyzer.calculate_threshold_alpha()
print(f"Calculated Threshold Alpha: {alpha}")

# Detect outliers
outliers = analyzer.detect_outliers(alpha)
print(f"Detected Outliers: {outliers}")
