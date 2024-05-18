# Implementation for randomized quicksort algorithm

import random

# Function that rearranges elements in an array between two sides of a pivot.
def Partition(A, p, r):
    x = A[r] # Pivot
    i = p - 1 # Highest index of the low side
    # Iterate through each element other than the pivot
    for j in range(p, r): 
        # Check if element belongs on the low side
        if A[j] <= x:
            # Index of a new low side element
            i = i + 1 
            # Swap A[i] with A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    # Pivot must be placed between the low and high sides
    # Swap A[i + 1] with A[r]
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    # Index of the pivot
    return i + 1

# Function that randomly selects a pivot and initiates Partition.
def Randomized_Partition(A, p, r):
    # Randomly select a pivot
    i = random.randint(p, r)
    # Swap A[r] with A[i]
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return Partition(A, p, r)

# Function that sorts an array using the randomized quicksort algorithm.
def Randomized_Quicksort(A, p, r):
    if p < r:
        q = Randomized_Partition(A, p, r)
        Randomized_Quicksort(A, p, q - 1)
        Randomized_Quicksort(A, q + 1, r)

# Test Case 1
arr1 = [2, 1, 7, 8, 3, 5, 6, 4]
print('Original Array:', arr1)
Randomized_Quicksort(arr1, 0, len(arr1) - 1)
print('Sorted Array:', arr1, '\n')

# Test Case 2
arr2 = [12, 11, 13, 5, 6, 7, 1, 3, 4, 9, 8, 10, 2, 15, 14]
print('Original Array:', arr2)
Randomized_Quicksort(arr2, 0, len(arr2) - 1)
print('Sorted Array:', arr2)
