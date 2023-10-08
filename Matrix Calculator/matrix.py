''' Functions related to matrix. '''

def matrix(m,n):
    ''' Accept order of the matrix and asking user to enter all elements of the matrix. '''
    ''' Return the matrix as a nested list with each row as an element of list '''
    L = []
    for i in range(m):
        l = []
        for j in range (n):
            e = eval(input(f"Enter A{i+1}{j+1}:"))
            l.append(e)
        L.append(l)
    return L


def display_matrix(M):
    ''' Displaying the nested list M like a matrix. '''
    for mr in M:
        print('[' , end = ' ')
        for me in mr:
            print(me , end = ' ')
        print(']')


def det_2(M):
    ''' Return the determinant of matrix A of order 2.'''
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]


def det_3(M):
    ''' Return determinant of A of order 3.'''
    l = []
    for i in range(3):
        l.append(cofactor_matrix_3(M)[0][i] * M[0][i])
    return l[0] + l[1] + l[2]


def display_det(M):
    ''' Displaying the nested list M in a determinant form.'''
    for mr in M:
        print('|' , end = ' ')
        for me in mr:
            print(me , end = ' ')
        print('|')

def cofactor_matrix_2(M):         
    ''' Return matrix of cofactors of elements of matrix M of order 2.'''
    M[0][0],M[1][1] = M[1][1],M[0][0]
    M[0][1],M[1][0] = - M[1][0], - M[0][1]
    return M


def cofactor_matrix_3(M):
    ''' Return matrix of cofactors of elements of matrix M of order 3.'''
    C = []
    for i in range(3):
        R = []
        for j in range(3):
            E = []
            for a in range(3):
                e = []
                for b in range(3):
                    if a != i and b != j:
                        sign = (-1)**(a+b)
                        e.append(sign * M[a][b])
                if e != []:
                    E.append(e)      
            R.append(det_2(E))
        C.append(R)
    return C


def transpose_matrix(M,m,n):
    ''' Return transpose matrix of matrix M.'''
    T = []  
    for i in range(n):
        t = []
        for j in range(m):
            t.append(M[j][i])
        T.append(t)
    return T


def display_inverse(M,det):
    ''' Displaying the nested list M in a determinant form with determinant.'''
    id = f"1 / {det}"
    print(id , end = ' ')
    for mr in M:
        print('[' , end = ' ')
        for me in mr:
            print(me , end = ' ')
        print(']')
        print(' '*len(id) , end = ' ')
