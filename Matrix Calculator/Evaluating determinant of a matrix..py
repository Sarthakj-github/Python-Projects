# Finding determinant of matrix of order 2 and 3.

from matrix import *

# Taking details of matrix A.
n = int(input("Enter order of square matrix A(2 or 3):"))
print("For Matrix A:-")
A = matrix(n,n)

# For |A|.

if n == 2:         # For order 2.
    print("Determinant of matrix A:-")
    display_det(A)
    print("is",det_2(A))

elif n == 3:       # For order 3.
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

    print("Determinant of matrix A:-")
    display_det(A)
    print("is",det_3(detA))

                
