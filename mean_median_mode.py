import numpy as np

data = np.array([23, 22, 22, 23, 24, 24, 23, 22, 21, 24, 23])
mean = np.mean(data)  # calculates the mean
print("Mean: ", round(mean, 2))  # Mean:  22.82

median = np.median(data)  # calculates the median
print("Median: ", median)  # Median:  23.0

from scipy import stats

data = np.array([23, 22, 22, 23, 24, 24, 23, 22, 21, 24, 23])
mode_age = stats.mode(data)  # calculates the mode
print("Mode: ", mode_age.mode)  # Mode:  23

data = np.array([20, 21, 21, 23, 23, 24]) # Handling Ties in Mode with `scipy`
mode = stats.mode(data)
print("Mode: ", mode.mode)  # Mode: 21