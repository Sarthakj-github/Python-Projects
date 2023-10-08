# Adding two matrices.

from matrix import *

# Taking order of A and B.
m = int(input("Enter no. of rows(m):"))
n = int(input("Enter no.of columns(n):"))

# Taking elements of A.
print("For Matrix A:-")
A = matrix(m,n)

# Taking elements of B.
print("For Matrix B:-")
B = matrix(m,n)
    
# Adding elements of A and B and making new matrix.
S = []     # Initial summed matrix 
for i,j in zip(A,B):
    s = []
    for a,b in zip(i,j):
        s.append(a+b)
    S.append(s)

# Displaying the matrix obtained by adding A and B.
print("Summed Matrix:-")
display_matrix(S)
