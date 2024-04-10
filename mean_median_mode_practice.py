import numpy as np
from scipy import stats

# age_group = np.array([8, 9, 8, 10, 10, 9, 10, 10, 11, 8, 10])
# mean_age_group = np.mean(age_group) 
# median_age_group = np.median(age_group) 
# mode_age_group = stats.mode(age_group)

# print("Mean age: ", mean_age_group)
# print("Median age: ", median_age_group)
# print("Mode age: ", mode_age_group.mode)

ages = np.array([15, 26, 27, 25, 26, 27, 28, 26, 27, 28, 50])
mean_age = np.mean(ages)
median_age = np.median(ages)
mode_age = stats.mode(ages)

print("Mean Age: ", mean_age)
print("Median Age: ", median_age)
print("Mode Age: ", mode_age.mode)

ages_group_2 = np.array([25, 24, 26, 24, 25, 25, 24, 26, 27, 24, 26])
# TODO: Compute the mean of the ages group.
mean_ages_group_2 = np.mean(ages_group_2)
# TODO: Compute the median of the ages group.
median_ages_group_2 = np.median(ages_group_2)
mode_2 = stats.mode(ages_group_2)

print("For the second age group:")
print("Mean: ", mean_ages_group_2)
print("Median: ", median_ages_group_2)
print("Mode: ", mode_2.mode)

# Our space camp students' ages
kids_ages = np.array([8, 9, 9, 10, 7, 6, 10, 9, 7, 8, 9]) 

# TODO: Compute their mean age
kid_mean_age = np.mean(kids_ages)
# TODO: Determine their median age
kid_median_age = np.median(kids_ages)
# TODO: Figure out the most frequent age
kid_mode_age = stats.mode(kids_ages)
# Let's print our findings
print("For the average age, middle age, and most common age of these little astronauts")
print("Their Mean is: ", kid_mean_age)
print("Their Median is: ", kid_median_age)
print("Their Mode (most common age) is: ", kid_mode_age.mode)