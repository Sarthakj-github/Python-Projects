# Finding cofactors of elements of the matrix.

from matrix import *

n = int(input("Enter the order of square matrix:"))
print("For matrix A:-")
A = matrix(n,n)

# Making a matrix of all cofactors of elements in the matrix A.

C = []        # Initial matrix of cofactors.

if n == 2:    # For matrix of order 2.
    A[0][0],A[1][1] = A[1][1],A[0][0]
    A[0][1],A[1][0] = - A[1][0], - A[0][1]
    C = A
elif n == 3:  # For matrix of order 3.
    for i in range(n):
        R = []
        for j in range(n):
            E = []
            for a in range(n):
                e = []
                for b in range(n):
                    if a != i and b != j:
                        sign = (-1)**(a+b)
                        e.append(sign * A[a][b])
                if e != []:
                    E.append(e)      
            R.append(det_2(E))
        C.append(R)

print("Matrix of cofactors of elements of matrix A:-")
display_matrix(C)
