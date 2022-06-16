# Multiply two square matrices of order n by thedefinition based algorithm
# input: two n-by-n matrices A and B
# output: matrix C = AB

import random
import time
from strassen import split, strassen

def matrix_multiplication(A, B):
    t_start = time.time()
    C = []
    for i in range(len(A)):
        col_C =[]
        for j in range(len(B[i])):
            x = 0
            for k in range(len(B)):
                x += A[i][k] * B[k][j]
            col_C.append(x)
        C.append(col_C)
    t_finish = time.time()
    print('execution time=', t_finish - t_start)
    return C

if __name__ == "__main__":
    print('insert n for n-by-n matrices A and B')
    n = int(input())
    rows, cols = (n, n)

# set the matrices A, B, and C

# method 1
# A = [[random.randint(0,9) for i in range(cols)] for j in range(rows)]
# B = [[random.randint(0,9) for i in range(cols)] for j in range(rows)]
# C = [[0 for i in range(cols)] for j in range(rows)]

# method 2
    A = []
    B = []
    for i in range(rows):
        col_A = []
        col_B = []
        for j in range(cols):
            col_A.append(random.randint(0, 9))
            col_B.append(random.randint(0, 9))
        A.append(col_A)
        B.append(col_B)

    C = matrix_multiplication(A, B)

    # D = strassen(A, B)
    # print(C)



# print('A =', A)
# print('B =', B)
# print('C =', C)

