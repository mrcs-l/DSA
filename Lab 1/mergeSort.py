# Implementation for merge sort algorithm

# Function that initiates the merge sort algorithm
def merge_sort(arr, length):
    merge_sort_recursion(arr, 0, length - 1)

# Helper function that recursively divides the array into sorted subarrays
def merge_sort_recursion(arr, left, right):
    # Check if the array can be divided into further subarrays
    if left < right:
        # Get the middle index
        mid = left + (right - left) // 2
        # Recursively divide the LHS and RHS subarrays in half
        merge_sort_recursion(arr, left, mid)
        merge_sort_recursion(arr, mid + 1, right)
        # Merge the sorted subarrays
        merge_sorted_arrays(arr, left, mid, right)

# Function that merges two sorted subarrays
def merge_sorted_arrays(arr, left, mid, right):
    # Get the length of the LHS subarray (including the middle element)
    left_length = mid - left + 1
    # Get the length of the RHS subarray
    right_length = right - mid

    # Allocate temporary arrays to store the LHS and RHS subarrays
    temp_left = [0] * left_length
    temp_right = [0] * right_length

    # Iterate through the LHS and RHS subarrays, copying the elements to temporary arrays
    for i in range(left_length):
        temp_left[i] = arr[left + i]
    for i in range(right_length):
        temp_right[i] = arr[mid + 1 + i]

    # Set the initial indices to compare the elements in the LHS and the RHS
    i = 0; j = 0; k = left # k is the starting index of the main array

    # Loop through the LHS and RHS subarrays until one of them is exhausted
    while i < left_length and j < right_length:
        # Check if the element should be copied from the LHS
        if temp_left[i] <= temp_right[j]:
            # Copy the element to the main array
            arr[k] = temp_left[i]
            # Move the next element in the LHS
            i += 1
        else:
            # Copy the element from the RHS to the main array
            arr[k] = temp_right[j]
            # Move the next element in the RHS
            j += 1
        # Move to the next position in the main array
        k += 1

    # Loop through the remaining elements of the LHS
    while i < left_length:
        # The remaining elements are already sorted
        # so we can copy them directly to the main array
        arr[k] = temp_left[i]
        # Move to the next element in the LHS
        i += 1
        # Move to the next position in the main array
        k += 1
    
    # Loop through the remaining elements of the RHS
    while j < right_length:
        # Copy the element to the main array
        arr[k] = temp_right[j]
        # Move to the next element in the RHS
        j += 1
        # Move to the next position in the main array
        k += 1

#Test case 1
arr_1 = [12, 3, 7, 9, 14, 6, 11, 2]
merge_sort(arr_1, len(arr_1))
print(arr_1)

#Test case 2
arr_2 = [4, 9, 20, 12, 15, 7, 1, 2, 50, 32, 41, 30, 14, 8, 19, 25]
merge_sort(arr_2 , len(arr_2))
print(arr_2)