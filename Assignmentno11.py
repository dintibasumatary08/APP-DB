import pandas as pd
import random

# Create a Series of 10 random numbers
numbers = pd.Series([random.randint(1, 100) for i in range(10)])

print("Series:")
print(numbers)

# Indexing
print("\nNumber at index 2:")
print(numbers[2])

# Filtering
print("\nNumbers greater than 50:")
print(numbers[numbers > 50])

# Statistical operations
print("\nMean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())