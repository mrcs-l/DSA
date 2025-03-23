# Implementation for the recursive matrix multiplication algorithm.

# Function that adds two matrices together. 
def add_matrix(A, B, C, row, col, n):
    for i in range(n):
        for j in range(n):
            C[row + i][col + j] = A[i][j] + B[i][j]

# Helper function to perform the recursive matrix multiplication.
def multiply_matrix_recursive(A, B, C, rowA, colA, rowB, colB, rowC, colC, n):
    if n == 1: # Base case for when the matrix has reached a submatrix of size 1x1.
        C[rowC][colC] += A[rowA][colA] * B[rowB][colB]
        return
    
    # Divide the matrix into 4 submatrices.
    half = n // 2

    # C11 = A11 * B11 + A12 * B21
    multiply_matrix_recursive(A, B, C, rowA, colA, rowB, colB, rowC, colC, half) 
    multiply_matrix_recursive(A, B, C, rowA, colA + half, rowB + half, colB, rowC, colC, half) 

    # C12 = A11 * B12 + A12 * B22
    multiply_matrix_recursive(A, B, C, rowA, colA, rowB, colB + half, rowC, colC + half, half) 
    multiply_matrix_recursive(A, B, C, rowA, colA + half, rowB + half, colB + half, rowC, colC + half, half) 

    # C21 = A21 * B11 + A22 * B21
    multiply_matrix_recursive(A, B, C, rowA + half, colA, rowB, colB, rowC + half, colC, half) 
    multiply_matrix_recursive(A, B, C, rowA + half, colA + half, rowB + half, colB, rowC + half, colC, half) 

    # C22 = A21 * B12 + A22 * B22
    multiply_matrix_recursive(A, B, C, rowA + half, colA, rowB, colB + half, rowC + half, colC + half, half) 
    multiply_matrix_recursive(A, B, C, rowA + half, colA + half, rowB + half, colB + half, rowC + half, colC + half, half) 

# Function to initiate the matrix multiplication algorithm.
def multiply_matrix(A, B, C, n):
    multiply_matrix_recursive(A, B, C, 0, 0, 0, 0, 0, 0, n)

# Test cases
print("Test case 1:")

matrixA = [
    [5, 2, 6, 1],
    [0, 6, 2, 0],
    [3, 8, 1, 4],
    [1, 8, 5, 6]
]
print("\nMatrix A")
for row in matrixA:
    print(row)

matrixB = [
    [7, 5, 8, 0],
    [1, 8, 2, 6],
    [9, 4, 3, 8],
    [5, 3, 7, 9]
]
print("\nMatrix B")
for row in matrixB:
    print(row)

n = 4 # 4x4 matrices
matrixC = [[0 for i in range(n)] for j in range(n)] # Set all elements for matrix C to 0

multiply_matrix(matrixA, matrixB, matrixC, n) # A * B = C

print("\nMatrix C")
for row in matrixC:
    print(row)

print("\nTest case 2:") 

n = 16 # 16x16 matrices 
matrixA = [[i for i in range(n)] for j in range(n)] 
matrixB = [[i for i in range(n)] for j in range(n)] 
matrixC = [[0 for i in range(n)] for j in range(n)] # Set all elements for matrix C to 0

print("\nMatrix A")
for row in matrixA:
    print(row)

print("\nMatrix B")
for row in matrixB:
    print(row)

multiply_matrix(matrixA, matrixB, matrixC, n) # A * B = C

print("\nMatrix C")
for row in matrixC:
    print(row)