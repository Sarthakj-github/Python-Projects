# Finding transpose of the matrix.

from matrix import *

# Taking details of matrix A.
n = int(input("Enter order of square matrix A:"))
print("For Matrix A:-")
A = matrix(n,n)

# For A transpose.
T = []  # Initial transpose matrix.
for i in range(n):
    t = []
    for j in range(n):
        t.append(A[j][i])
    T.append(t)

# Displaying the transpose of A.
print("Transpose Matrix:-")
display_matrix(T)
