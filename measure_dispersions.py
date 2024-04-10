import numpy as np

# Test scores of five students
scores = np.array([72, 88, 80, 96, 85])

# Calculate and print the Range
range_scores = np.ptp(scores)
print(f"Range of scores: {range_scores}")  # Range of scores: 24

# Test scores of five students
scores = np.array([72, 88, 80, 96, 85])

# Calculate and print the Variance
variance_scores = np.var(scores)
print(f"Variance of scores: {variance_scores}")  # Variance of scores: 64.16

# Test scores of five students
scores = np.array([72, 88, 80, 96, 85])

# Calculate and print the Standard Deviation
std_scores = np.std(scores)
print(f"Standard deviation of scores: {std_scores}")  # Standard deviation of scores: 8.01