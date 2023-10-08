# Subtracting one matrix from other.

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
    
# Subtracting elements of B from A and making new matrix.
D = []     # Initial subtracted matrix 
for i,j in zip(A,B):
    d = []
    for a,b in zip(i,j):
        d.append(a-b)
    D.append(d)

# Displaying the matrix obtained by subtracting B from A.
print("Subtracted Matrix:-")
display_matrix(D)
