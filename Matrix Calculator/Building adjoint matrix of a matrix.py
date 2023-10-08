# Making adjoint of a matix.

from matrix import *

# Taking matrix A for adjointing.
n = int(input("Enter order of square matrix:"))
A = matrix(n,n)

# For finding adjoint of A.

# For order 2.
if n == 2:
    Adj = transpose_matrix(cofactor_matrix_2(A),n)

# For order 3.
elif n == 3:
    Adj = transpose_matrix(cofactor_matrix_3(A),n)

print("Adjoint matrix of matrix A:-")
display_matrix(Adj)

