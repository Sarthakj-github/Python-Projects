# Multiplying two matrices.

from matrix import *

# Taking order and elements of first matrix.
print("For Matrix A:-")
ma = int(input("Enter no. of rows(m):"))
na = int(input("Enter no.of columns(n):"))
A = matrix(ma,na)

# Taking order and elements of second matrix.
print("For Matrix B:-")
mb = int(input("Enter no. of rows(m):"))
nb = int(input("Enter no.of columns(n):"))
B = matrix(mb,nb)

# Taking Product of two marices.
if na != mb:  # Checking condition of mul.of matrices.
    print("No. of columns of A should be equal to no. of rows of B.")

else:
    P = []
    for r in range(ma):
        p = []
        for c in range(nb):
            E = 0
            for s in range(na):
               e = A[r][s] * B[s][c]
               E += e
            p.append(E)
        P.append(p)

# Displaying the matrix obtained by adding A and B.
print("Multiplied Matrix :-")
display_matrix(P)
