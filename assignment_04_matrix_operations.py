# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Matrix Operations

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Row must have", cols, "values.")
            return None
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end="  ")
        print()

# Part A: Transpose
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

# Part B: Add Two Matrices
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(A[i][j] + B[i][j])
        result.append(new_row)
    return result

# Part C: Multiply Two Matrices
def multiply_matrices(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    
    if colsA != rowsB:
        print("Error: Columns of A must equal rows of B.")
        return None
    
    result = []
    for i in range(rowsA):
        new_row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

def main():
    # Example: Transpose
    print("=== Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    A = read_matrix(m, n)
    if A:
        print("\nOriginal Matrix:")
        print_matrix(A)
        T = transpose(A)
        print("\nTransposed Matrix:")
        print_matrix(T)

    # Example: Add Two Matrices
    print("\n=== Add Two Matrices ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    print("Matrix A:")
    A = read_matrix(m, n)
    print("Matrix B:")
    B = read_matrix(m, n)
    if A and B:
        print("\nResult (A + B):")
        print_matrix(add_matrices(A, B))

    # Example: Multiply Two Matrices
    print("\n=== Multiply Two Matrices ===")
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter cols for Matrix A: "))
    print("Matrix A:")
    A = read_matrix(m, n)
    p = int(input("Enter cols for Matrix B: "))
    print("Matrix B:")
    B = read_matrix(n, p)
    if A and B:
        print("\nResult (A x B):")
        result = multiply_matrices(A, B)
        if result:
            print_matrix(result)


main()
