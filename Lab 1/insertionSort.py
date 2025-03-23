# Implementation for insertion sort algorithm

# Function for insertion sort algorithm
def insertion_sort(arr):
    # Iterate through the array starting from the second element
  for i in range(1, len(arr)):
    # Get the current element to be inserted
    key = arr[i]

    # Store the index before the current element
    j = i - 1
    # Check for remaining elements in the sorted subarray which are greater than the key
    while j >= 0 and arr[j] > key:
      # Shift the elements in the sorted subarray [j..i-1] to the right by one position to make space for the key
      arr[j + 1] = arr[j]
      # Move down from the right-most element to the left-most element of the sorted subarray
      j = j - 1
    # Found the correct position j, to insert the key
    arr[j + 1] = key

# Test case 1
arr_1 = [5, 2, 4, 6, 1, 3]
insertion_sort(arr_1)
print(arr_1)

# Test case 2
arr_2 = [3, 14, 9, 1, 10, 5, 30, 27, 50, 17]
insertion_sort(arr_2)
print(arr_2)