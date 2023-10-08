# Finding A inverse.

from matrix import *

n = int(input("Enter the order of square matrix:"))
print("For matrix A:-")
A = matrix(n,n)

# Solving for A inverse.

# For order 2.
if n == 2:
    Adj = transpose_matrix(cofactor_matrix_2(A),n)
    detA = det_2(A)
    if detA == 0:
        print("A inverse will not exist , since detA = 0.")
    else:
        print("A inverse of matrix A:-")
        display_inverse(Adj,detA)

# For order 3.
elif n == 3:
    Adj = transpose_matrix(cofactor_matrix_3(A),n
    detA = []      # List of last 3 numbers for matrix addition.
    for a in range(n):
        E = []     # Nested list of each element det. expansion in R1.
        for i in range(n):
            e = [] 
            for j in range(n):
                if i != 0 and j != a:
                    e.append(A[i][j])
            if e != []:    
                E.append(e)
        detA.append(det_2(E) * A[0][a])
    detA = det_3(detA)
    if detA == 0:
        print("A inverse will not exist , since detA = 0.")
    else:
        print("A inverse of matrix A:-")
        display_inverse(Adj,detA)
