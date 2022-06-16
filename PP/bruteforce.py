import numpy as np

def brute_force(A, B):
    '''
    .shape = untuk mengetahui jumlah baris dan kolom
    masing2 matrix
    m = banyak elemen di kolom/baris A&B
    k = elemen ke (ex: C11)
    n = banyak elemen di baris mA
    p = banyak elemen di kolom mB
    '''
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    ''' tampung hasil perkalian matrix ke matrix c'''
    C = np.array([[0]*p for i in range(n)])
    '''perkalian matrix'''
    for i in range(n):
        for j in range(p):
            for k in range(m): 
                C[i][j] += A[i][k]*B[k][j]
    return C