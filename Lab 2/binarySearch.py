# Implementation for binary search algorithm

# Function to initiate the binary search algorithm
def binary_search(arr, n, target):
    return binary_search_recursive(arr, 0, n - 1, target)

# Helper function to perform the recursive binary search.
def binary_search_recursive(arr, low, high, target):
    # Base case for when the element is not found.
    if high < low: 
        return -1
    
    # Find the middle index of the array
    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid # Target found
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target) # Search the left half
    else:
        return binary_search_recursive(arr, mid + 1, high, target) # Search the right half

# Test case 1
arr1 = [3, 5, 7, 8, 9, 12, 15] # Sorted array
target = 9
n = len(arr1) 
print(f"Search for element {target} in {arr1}")

result = binary_search(arr1, n, target)
if result != -1:
    print(f"Element found at index {result}\n")
else:
    print("Element is not present in array\n")

# Test case 2
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Sorted array
target = 11
n = len(arr2)
print(f"Search for element {target} in {arr2}")

result = binary_search(arr2, n, target)
if result != -1:
    print(f"Element found at index {result}\n")
else:
    print("Element was not found in the array\n")
