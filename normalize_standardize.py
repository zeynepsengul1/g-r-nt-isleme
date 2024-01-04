import numpy as np

def normalize(data):

    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def standardize(data):

    mean_val = np.mean(data)
    std_dev = np.std(data)
    standardized_data = (data - mean_val) / std_dev
    return standardized_data


data = np.array([1, 2, 3, 4, 5], dtype=float)

normalized_result = normalize(data)
standardized_result = standardize(data)

print("Original Data:", data)
print("Normalized Data:", normalized_result)
print("Standardized Data:", standardized_result)