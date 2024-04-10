import numpy as np

# Performance scores of students in math class
math_scores = np.array([88, 92, 80, 90, 85, 93, 78, 88, 79, 94])

# Calculate and print the Range
range_scores = np.ptp(math_scores)
print(f"Range of math scores: {range_scores}")

# Calculate and print the Variance
variance_scores = np.var(math_scores)
print(f"Variance of math scores: {variance_scores}")

# Calculate and print the Standard Deviation
std_scores = np.std(math_scores)
print(f"Standard deviation of math scores: {std_scores}")

# Data for the final marks of seven students out of 100 in English
english_marks = np.array([90, 85, 45, 92, 88, 76, 95])

# Calculate and print the Range of the marks
range_english = np.ptp(english_marks)
print(f"Range of marks: {range_english}")

# Calculate and print the Variance of the marks
variance_english = np.var(english_marks)
print(f"Variance of marks: {variance_english}")

# Calculate and print the Standard Deviation of the marks
std_english = np.std(english_marks)
print(f"Standard deviation of marks: {std_english}")

# Grades of students in math examination
math_scores = np.array([70, 80, 100, 95, 65, 90])

# Calculate and print the Range, Variance, Standard Deviation
range_scores = np.ptp(math_scores)
variance_scores = np.var(math_scores)
std_scores = np.std(math_scores)
print(f"Range of scores: {range_scores}")
print(f"Variance of scores: {variance_scores}")
print(f"Standard deviation of scores: {std_scores}")

# Educational performance scores
scores = np.array([55, 45, 67, 89, 73, 56, 60, 65, 66, 54])

# Calculate and print the Range
range_scores = np.ptp(scores)
print(f"Range of student scores: {np.ptp(scores)}")

# Calculate and print the Variance
variance_scores = np.var(scores)
print(f"Variance of student scores: {np.var(scores):.2f}")

# TODO: Calculate and print the Standard Deviation in one line
std_scores = np.std(scores)
print(f"Standard deviation of scores: {np.std(scores):.2f}")

# Scores of students in mathematics
math_scores = np.array([95, 78, 63, 90, 85, 77, 82, 91, 70])

# TODO: Calculate the Range of the scores and print it
range_math_scores = np.ptp(math_scores)
print(f"Range of students' mathematics scores: {np.ptp(math_scores)}")
# TODO: Calculate the Variance of the scores and print it
variance_math_scores = np.var(math_scores)
print(f"Variance of students' mathematics scores: {np.var(math_scores):.2f}")
# TODO: Calculate the Standard Deviation of the scores and print it
std_math_scores = np.std(math_scores)
print(f"Standard deviation of students' mathematics scores: {np.std(math_scores):.2f}")