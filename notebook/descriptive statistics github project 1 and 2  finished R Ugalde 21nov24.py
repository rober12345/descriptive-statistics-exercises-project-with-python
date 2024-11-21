# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:52:00 2024

@author: rober ugalde
https://miniature-space-bassoon-494pvv497jqhjrj6.github.dev/
exercise 1 and 2



Descriptive statistics problems
Exercise 1
We will use NumPy to obtain information to describe statistically.

Generate an array of 100 elements following a normal distribution.
Generate an array of 100 elements following a chi-square distribution with 3 degrees of freedom.
Calculate the main metrics and statistical measures that best describe the two vectors.

"""



import numpy as np

# Generate an array of 100 elements following a normal distribution
normal_array = np.random.normal(loc=0, scale=1, size=100)

# Generate an array of 100 elements following a chi-square distribution with 3 degrees of freedom
chi_square_array = np.random.chisquare(df=3, size=100)

# Calculate descriptive statistics for the normal array
normal_stats = {
    'Mean': np.mean(normal_array),
    'Median': np.median(normal_array),
    'Variance': np.var(normal_array),
    'Standard Deviation': np.std(normal_array),
    'Min': np.min(normal_array),
    'Max': np.max(normal_array)
}

# Calculate descriptive statistics for the chi-square array
chi_square_stats = {
    'Mean': np.mean(chi_square_array),
    'Median': np.median(chi_square_array),
    'Variance': np.var(chi_square_array),
    'Standard Deviation': np.std(chi_square_array),
    'Min': np.min(chi_square_array),
    'Max': np.max(chi_square_array)
}

# Print results
print("Descriptive Statistics for Normal Distribution:")
for key, value in normal_stats.items():
    print(f"{key}: {value:.2f}")

print("\nDescriptive Statistics for Chi-Square Distribution:")
for key, value in chi_square_stats.items():
    print(f"{key}: {value:.2f}")


"""
Exercise 2
Write a Python program to calculate the standard deviation of the following data:

data = [4, 2, 5, 8, 6]

"""
import numpy as np

# Data
data = [4, 2, 5, 8, 6]

# Calculate the standard deviation
std_deviation = np.std(data)

# Print the result
print(f"Standard Deviation of the data: {std_deviation:.2f}")


