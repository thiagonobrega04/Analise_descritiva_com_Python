import pandas as pd
import numpy as np

scores = np.array([76, 85, 67, 45, 89, 70, 92, 82])

# Calculate median
median_w1 = np.percentile(scores, 50)
print(median_w1)  # Output: 79.0
# Check if it is the same as median
median_w2 = np.median(scores)
print(median_w2)  # Output 79.0

# Calculate Q1 and Q3
Q1 = np.percentile(scores, 25)
print(Q1)  # Output: 69.25
Q3 = np.percentile(scores, 75)
print(Q3)  # Output: 86.0

math_scores = pd.DataFrame({
  'Name': ['Jerome', 'Jessica', 'Jeff', 'Jennifer', 'Jackie', 'Jimmy', 'Joshua', 'Julia'],
  'Score': [56, 13, 54, 48, 49, 100, 62, 55]
})

# IQR for scores
Q1 = np.percentile(math_scores['Score'], 25)
print(Q1)
Q3 = np.percentile(math_scores['Score'], 75)
print(Q3)
IQR_score = Q3 - Q1
print(IQR_score)  # Output: 8.75

# Finding Outliers
scores = math_scores['Score']  # to simplify next expression
outliers_scores = scores[(scores < Q1 - 1.5 * IQR_score) | (scores > Q3 + 1.5 * IQR_score)]
print(outliers_scores)  # Outputs 13 and 100