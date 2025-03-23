# Implementation for Heapsort algorithm

# Function that maintains the max-heap property. 
def Max_Heapify(A, i, heap_size):
    left = 2 * i # left child
    right = 2 * i + 1 # right child
    # Check if left child is greater than the parent
    if left < heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i # Parent is greater than the left child
    # Check if right child is greater than the parent
    if right < heap_size and A[right] > A[largest]:
        largest = right
    # Check if the largest element is not the parent
    if largest != i:
        #Swap A[i] with A[largest]
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        Max_Heapify(A, largest, heap_size) # Recursively maintain the max-heap property

# Function that converts an array into a max-heap in a bottom up manner. 
def Build_Max_Heap(A):
    heap_size = len(A)
    # Iterate through the array from the last non-leaf node to the root node
    for i in range(heap_size // 2, -1, -1):
        Max_Heapify(A, i, heap_size)

# Function that sorts the array using heapsort algorithm.
def Heapsort(A):
    Build_Max_Heap(A) # Largest element stored at the root
    heap_size = len(A)
    # Iterate through the heap from the last element to the second element
    for i in range(heap_size - 1, 0, -1):
        # Swap A[0] with A[i] 
        # Moving the largest element to the last position of the heap
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        # Remove the largest element from the heap
        heap_size = heap_size - 1
        # Restore the max-heap property
        Max_Heapify(A, 0, heap_size)

# Test Case 1
A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("Original Array: ", A)
Heapsort(A)
print("Sorted Array: ", A, "\n")

# Test Case 2
B = [4, 1, 12, 3, 2, 5, 9, 10, 11, 6, 7, 8, 15, 14, 13] 
print("Original Array: ", B)
Heapsort(B)
print("Sorted Array: ", B)