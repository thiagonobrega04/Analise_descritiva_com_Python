import pandas as pd
import numpy as np

grades = np.array([73, 85, 77, 85, 91, 72, 69, 77, 83, 76, 78, 81])

# Calculate Q1, Q2, Q3
Q1 = np.percentile(grades, 25)
print(Q1)
Q2 = np.percentile(grades, 50)
print(Q2)
Q3 = np.percentile(grades, 75)
print(Q3)

# Calculate IQR
IQR = Q3 - Q1

print("The Interquartile Range of the student grades is: ", IQR)

math_scores = np.array([92, 75, 88, 78, 90, 80, 88, 80]) 
  
# Calculate Q1 and Q3 for math scores
Q1_math = np.percentile(math_scores, 25)
print(f"The first quartile (Q1) of the math scores is {Q1_math}\n")
Q3_math = np.percentile(math_scores, 75)
print(f"The third quartile (Q3) of the math scores is {Q3_math}\n")

# Calculate the Interquartile Range for math scores
IQR_math = Q3_math - Q1_math
print(f"The interquartile range (IQR) for the math scores is {IQR_math}")

upper_outlier_bound = Q3_math + 1.5 * IQR_math

#calculate lower outlier bound
lower_outlier_bound = Q1_math - 1.5 * IQR_math

# Print values of upper and lower bounds
print("\nUpper Outlier Bound:", upper_outlier_bound)
print("Lower Outlier Bound:", lower_outlier_bound)

student_scores = np.array([88, 91, 76, 84, 100, 78, 92, 68])

# Calculate Q1 and Q3
Q1 = np.percentile(student_scores, 25)
print(f"The first quartile (Q1) of the students' scores are {Q1}\n")
Q3 = np.percentile(student_scores, 75)
print(f"The third quartile (Q3) of the students' scores are {Q3}\n")

#Calculate Interquartile Range
IQR = Q3 - Q1

print(f"The interquartile range (IQR) for the students' scores are {IQR}")

# We have collected the scores of a group of students in a mathematics test 
math_scores = np.array([78, 82, 85, 90, 92, 95, 73, 85, 86, 77, 83, 89, 94, 79, 75, 87])

# TODO: Calculate the first quartile (Q1)
Q1 = np.percentile(math_scores, 25)  # TODO: replace 0 with correct value

# TODO: Calculate the third quartile (Q3)
Q3 = np.percentile(math_scores, 75)  # TODO: replace 0 with correct value

# TODO: Calculate the Interquartile Range (IQR)
IQR_math_scores = Q3 - Q1

print(IQR_math_scores)

grades = np.array([78, 72, 84, 67, 69, 95, 92, 85, 77, 88, 75])

# TODO: Calculate and print the median of the grades
median = np.median(grades)
print(median)      

# TODO: Calculate the first and third quartiles of the grades
Q1 = np.percentile(grades, 25)
print(Q1)
Q3 = np.percentile(grades, 75)
print(Q3)

# TODO: Using the quartiles, calculate the Interquartile Range (IQR) and print it.
IQR = Q3 - Q1
print(IQR)