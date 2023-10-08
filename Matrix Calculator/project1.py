import tkinter as tk

from numpy import *
import numpy.matlib as mat

from matrix import *

root = tk.Tk()

title = root.title("MATRIX CALCULATOR")

geometry = root.geometry('1000x1000')

button1 = tk.Button(root,text = 'Addition of two matrices',bg  = 'red',height=2,width=30,font=2,command = lambda: first("ADDITION OF TWO MATRICES"))
button1.pack(pady=10)

button2 = tk.Button(root,text = 'Adjoint of a matrix',bg  = 'red',height=2,width=30,font=2,command = lambda: second("ADJOINT OF A MARTIX"))
button2.pack(pady=10)

button3 = tk.Button(root,text = 'Inverse of a matrix',bg  = 'red',height=2,width=30,font=2,command = lambda: third("INVERSE OF A MATRIX"))
button3.pack(pady=10)

button4 = tk.Button(root,text = 'Determinant of a matrix',bg  = 'red',height=2,width=30,font=2,command  = lambda: fourth("DETERMINANT OF A MATRIX"))
button4.pack(pady=10)

button5 = tk.Button(root,text = 'Transpose of a matrix',bg  = 'red',height=2,width=30,font=2,command = lambda: fifth("TRANSPOSE OF A MATRIX"))
button5.pack(pady=10)

button6 = tk.Button(root,text = 'Cofactor of elements of a matrix',bg  = 'red',height=2,width=30,font=2,command = lambda: sixth("COFACTOR OF ELEMENTS OF A MATRIX"))
button6.pack(pady=10)

button7 = tk.Button(root,text = 'Multiplication of two matrices',bg  = 'red',height=2,width=30,font=2,command = lambda: seventh("MULTIPLICATION OF TWO MATRICES"))
button7.pack(pady=10)

button8 = tk.Button(root,text = 'Subtraction on two matrices',bg  = 'red',height=2,width=30,font=2,command = lambda: eighth("DIFFERENCE OF TWO MATRICES"))
button8.pack(pady=10)

def first(ttl):
    root1a = tk.Toplevel(root)
    title1a = root1a.title(ttl)
    geometry1a = root1a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root1a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root1a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root1a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root1a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root1a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root1a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    
    
    label3 = tk.Label(root1a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=10)

    sa = tk.StringVar()

    entry1 = tk.Entry(root1a, bd=5, width=150, textvariable=sa).pack(pady=20)

    label4 = tk.Label(root1a, text='MATRIX B', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=10)

    sb = tk.StringVar()

    entry2 = tk.Entry(root1a, bd=5, width=150, textvariable=sb).pack(pady=20)

    caution = tk.Label(root1a, text='* Order of A = Order of B', height=1, width=50, font='Times 18 bold', fg='red').pack(pady=20)


    def result(a, b):
        A = mat.matrix(a).tolist()
        B = mat.matrix(b).tolist()

        root1b = tk.Toplevel(root1a)
        title1b = root1b.title('ADDITION OF TWO MATRICES')
        geometry1b = root1b.geometry('1000x1000')

        Sum_matrix = [[A[i][j] + B[i][j] for j in range(len(B[0]))] for i in range(len(A))]

        str_matrix = ''
        for i in Sum_matrix:
            str_matrix += str(i) + '\n'

        labela = tk.Label(root1b, text='RESULT MATRIX OF A + B', height=2, width=30, font='Times 18 bold italic',bg='magenta').pack(pady=100)

        labelb = tk.Label(root1b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root1b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root1b.destroy).pack()
        
    button = tk.Button(root1a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa), value(sb))).pack()

    buttonE = tk.Button(root1a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root1a.destroy).pack(pady=8)
    
def second(ttl):
    root2a = tk.Toplevel(root)
    title2a = root2a.title(ttl)
    geometry2a = root2a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root2a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root2a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root2a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root2a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root2a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root2a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root2a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root2a, bd=5, width=150, textvariable=sa).pack(pady=10)

    caution = tk.Label(root2a, text='* Matrix should be a Square matrix', height=1, width=50, font='Times 18 bold',fg='red').pack(pady=20)

    def result(a):
        A = mat.matrix(a).tolist()

        root2b = tk.Toplevel(root2a)
        title2b = root2b.title('ADJOINT OF A MATRIX')
        geometry2b = root2b.geometry('1000x1000')

        # For order 2.
        if len(A) == 2:
            Adj = transpose_matrix(cofactor_matrix_2(A), len(A),len(A))

        # For order 3.
        elif len(A) == 3:
            Adj = transpose_matrix(cofactor_matrix_3(A), len(A),len(A))


        str_matrix = ''
        for i in Adj:
            str_matrix += str(i) + '\n'

        labela = tk.Label(root2b, text='ADJOINT OF MATRIX A', height=2, width=30, font='Times 18 bold italic',bg='magenta').pack(pady=100)

        labelb = tk.Label(root2b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root2b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root2b.destroy).pack()

    button = tk.Button(root2a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa))).pack()

    buttonE = tk.Button(root2a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root2a.destroy).pack(pady=8)
    
def third(ttl):
    root3a = tk.Toplevel(root)
    title3a = root3a.title(ttl)
    geometry3a = root3a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root3a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root3a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root3a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root3a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root3a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root3a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root3a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root3a, bd=5, width=150, textvariable=sa).pack(pady=20)

    caution = tk.Label(root3a, text='* Matrix should be a Square matrix', height=1, width=50, font='Times 18 bold',fg='red').pack(pady=40)

    def result(a):
        A = mat.matrix(a).tolist()

        root3b = tk.Toplevel(root3a)
        title3b = root3b.title('INVERSE OF A MATRIX')
        geometry3b = root3b.geometry('1000x1000')

        # For oreder 2.
        if len(A) == 2:
            Adj = transpose_matrix(cofactor_matrix_2(A), len(A),len(A))
            det = det_2(A)

        # For order 3.
        elif len(A) == 3:
            Adj = transpose_matrix(cofactor_matrix_3(A), len(A),len(A))
            det = det_3(A)

        if det != 0:
            str_matrix = f'1/{det}'
            for i in Adj:
                str_matrix += str(i) + '\n'

        else:
            str_matrix = 'Inverse will not exist,'

        labela = tk.Label(root3b, text='INVERSE OF MATRIX A', height=2, width=30, font='Times 18 bold italic',bg='magenta').pack(pady=100)

        labelb = tk.Label(root3b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root3b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root3b.destroy).pack()

    button = tk.Button(root3a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa))).pack()

    buttonE = tk.Button(root3a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root3a.destroy).pack(pady=8)
    
def fourth(ttl):
    root4a = tk.Toplevel(root)
    title4a = root4a.title(ttl)
    geometry4a = root4a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root4a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root4a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root4a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root4a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root4a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root4a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root4a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root4a, bd=5, width=150, textvariable=sa).pack(pady=10)

    caution = tk.Label(root4a, text='* Matrix should be a Square matrix', height=1, width=50, font='Times 18 bold',fg='red').pack(pady=20)

    def result(a):
        A = mat.matrix(a).tolist()

        root4b = tk.Toplevel(root4a)
        title4b = root4b.title('DETERMINANT OF A MATRIX')
        geometry4b = root4b.geometry('1000x1000')

        # For oreder 2.
        if len(A) == 2:
            det = det_2(A)

        # For order 3.
        elif len(A) == 3:
            det = det_3(A)

        labela = tk.Label(root4b, text='DETERMINANT OF MATRIX A', height=2, width=30, font='Times 18 bold italic',bg='magenta').pack(pady=100)

        labelb = tk.Label(root4b, text=str(det), height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root4b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root4b.destroy).pack()

    button = tk.Button(root4a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa))).pack()

    buttonE = tk.Button(root4a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root4a.destroy).pack(pady=8)
    
def fifth(ttl):
    root5a = tk.Toplevel(root)
    title5a = root5a.title(ttl)
    geometry5a = root5a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root5a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root5a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root5a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root5a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root5a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root5a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label3 = tk.Label(root5a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root5a, bd=5, width=150, textvariable=sa).pack(pady=10)


    def result(a):
        A = mat.matrix(a).tolist()

        root5b = tk.Toplevel(root5a)
        title5b = root5b.title('TRANSPOSE OF A MATRIX')
        geometry5b = root5b.geometry('1000x1000')

        trsp = transpose_matrix(A,len(A),len(A[0]))

        str_matrix = ''
        for i in trsp:
            str_matrix += str(i) + '\n'

        labela = tk.Label(root5b, text='TRANSPOSE OF MATRIX A', height=2, width=30, font='Times 18 bold italic',
                      bg='magenta').pack(pady=100)

        labelb = tk.Label(root5b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root5b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root5b.destroy).pack()
    
    button = tk.Button(root5a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa))).pack()

    buttonE = tk.Button(root5a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root5a.destroy).pack(pady=8)
    
def sixth(ttl):
    root6a = tk.Toplevel(root)
    title6a = root6a.title(ttl)
    geometry6a = root6a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root6a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root6a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root6a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root6a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root6a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root6a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root6a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root6a, bd=5, width=150, textvariable=sa).pack(pady=10)

    caution = tk.Label(root6a, text='* Matrix should be a Square matrix', height=1, width=50, font='Times 18 bold',fg='red').pack(pady=20)

    def result(a):
        A = mat.matrix(a).tolist()

        root6b = tk.Toplevel(root6a)
        title6b = root6b.title('COFACTOR MATRIX OF A MATRIX')
        geometry6b = root6b.geometry('1000x1000')

        cftr = A
        if len(A) == 2:
            cftr = cofactor_matrix_2(A)

        elif len(A) == 3:
            cftr = cofactor_matrix_3(A)

        str_matrix = ''
        for i in cftr:
            str_matrix += str(i) + '\n'

        labela = tk.Label(root6b, text='COFACTOR MATRIX OF ELEMENTS OF A', height=2, width=40, font='Times 18 bold italic',
                          bg='magenta').pack(pady=100)

        labelb = tk.Label(root6b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)
        
        buttone = tk.Button(root6b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root6b.destroy).pack()
        
    button = tk.Button(root6a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa))).pack()

    buttonE = tk.Button(root6a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root6a.destroy).pack(pady=8)
    
def seventh(ttl):
    root7a = tk.Toplevel(root)
    title7a = root7a.title(ttl)
    geometry7a = root7a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root7a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root7a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root7a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root7a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root7a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root7a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root7a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root7a, bd=5, width=150, textvariable=sa).pack(pady=10)


    label4 = tk.Label(root7a, text='MATRIX B', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sb = tk.StringVar()

    entry2 = tk.Entry(root7a, bd=5, width=150, textvariable=sb).pack(pady=10)

    caution = tk.Label(root7a, text='* No. of columns of A = No. of rows of B', height=1, width=50,font='Times 18 bold',fg='red').pack(pady=20)

    def result(a, b):
        A = mat.matrix(a).tolist()
        B = mat.matrix(b).tolist()

        root7b = tk.Toplevel(root7a)
        title7b = root7b.title('MULTIPLICATION OF TWO MATRICES')
        geometry7b = root7b.geometry('1000x1000')

        str_matrix = ''
        if len(A[0]) != len(B):  # Checking condition of mul.of matrices.
            str_matrix = "No. of columns of A\nshould be equal to\nno. of rows of B."

        else:
            P = []
            for r in range(len(A)):
                p = []
                for c in range(len(B[0])):
                    E = 0
                    for s in range(len(A[0])):
                        e = A[r][s] * B[s][c]
                        E += e
                    p.append(E)
                P.append(p)


            for i in P:
                str_matrix += str(i) + '\n'

        labela = tk.Label(root7b, text='RESULT MATRIX OF A X B', height=2, width=30, font='Times 18 bold italic',
                          bg='magenta').pack(pady=100)

        labelb = tk.Label(root7b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root7b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root7b.destroy).pack()
        
    button = tk.Button(root7a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa), value(sb))).pack()

    buttonE = tk.Button(root7a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root7a.destroy).pack(pady=8)
    
def eighth(ttl):
    root8a = tk.Toplevel(root)
    title8a = root8a.title(ttl)
    geometry8a = root8a.geometry('1000x1000')

    def value(val):
        return val.get()

    label1 = tk.Label(root8a, text='HOW TO WRITE MATRIX IN ENTRY BOX:-', height=2, width=50, font='Times 18 bold italic',bg='yellow').pack()

    label2a = tk.Label(root8a,text='* Elements of a row are seperated by commas(,)', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2b = tk.Label(root8a,text='* Each row is seperated by semicolon(;)       ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2c = tk.Label(root8a,text='[a  b  c]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2d = tk.Label(root8a,text='[d  e  f]  --)  a, b, c; d, e, f; g, h, i', height=1, width=50, font='Times 18 bold',bg='yellow').pack()

    label2e = tk.Label(root8a,text='[g  h  i]                                         ', height=1, width=50, font='Times 18 bold',bg='yellow').pack()


    label3 = tk.Label(root8a, text='MATRIX A', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sa = tk.StringVar()

    entry1 = tk.Entry(root8a, bd=5, width=150, textvariable=sa).pack(pady=10)

    label4 = tk.Label(root8a, text='MATRIX B', height=2, width=15, font='Times 18 bold', bg='green').pack(pady=20)

    sb = tk.StringVar()

    entry2 = tk.Entry(root8a, bd=5, width=150, textvariable=sb).pack(pady=10)

    caution = tk.Label(root8a, text='* Order of A = Order of B', height=1, width=50,
                           font='Times 18 bold', fg='red').pack(pady=20)

    def result(a, b):
        A = mat.matrix(a).tolist()
        B = mat.matrix(b).tolist()

        root8b = tk.Toplevel(root8a)
        title8b = root8b.title('DIFFERENCE OF TWO MATRICES')
        geometry8b = root8b.geometry('1000x1000')

        diff_matrix = [[A[i][j] - B[i][j] for j in range(len(B[0]))] for i in range(len(A))]

        str_matrix = ''
        for i in diff_matrix:
            str_matrix += str(i) + '\n'

        labela = tk.Label(root8b, text='RESULT MATRIX OF A - B', height=2, width=30, font='Times 18 bold italic',
                          bg='magenta').pack(pady=100)

        labelb = tk.Label(root8b, text=str_matrix, height=5, width=20, font='Helvatic 18 bold', bg='blue').pack(pady=50)

        buttone = tk.Button(root8b,text='BACK',bg='red',height=1,width=8,font='Times 18 bold underline',command=root8b.destroy).pack()

    button = tk.Button(root8a, text="Submit", fg='blue', font=2, command=lambda: result(value(sa), value(sb)),).pack()

    buttonE = tk.Button(root8a,text='HOME',bg='red',height=1,width=8,font='Times 18 bold underline',command=root8a.destroy).pack(pady=8)
    
root.mainloop()

