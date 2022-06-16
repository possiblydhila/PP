import multiprocessing
import numpy as np
import time
#from pangkat import pangkat

def split(matrix):
    a = np.array(matrix)
    row, col = a.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def matrix_multiplication(A, B, result):
    for i in range(len(A)):
      col_C =[]
      for j in range(len(B[i])):
          x = 0
          for k in range(len(B)):
              x += A[i][k] * B[k][j]
          col_C.append(x)
      result.append(col_C)

def hitung(x, y):
    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """

    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = multiprocessing.Process(target=matrix_multiplication, args=(a, e, products,))
    p2 = multiprocessing.Process(target=matrix_multiplication, args=(b, g, products,))
    p3 = multiprocessing.Process(target=matrix_multiplication, args=(a, f, products,))
    p4 = multiprocessing.Process(target=matrix_multiplication, args=(b, h, products,))
    p5 = multiprocessing.Process(target=matrix_multiplication, args=(c, e, products,))
    p6 = multiprocessing.Process(target=matrix_multiplication, args=(d, g, products,))
    p7 = multiprocessing.Process(target=matrix_multiplication, args=(c, f , products,)) 
    p8 = multiprocessing.Process(target=matrix_multiplication, args=(d, h , products,)) 

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    # Computing the values of the 4 quadrants of the final matrix c
    '''c11 = p5 + p4 - p2 + p6 
    c12 = p1 + p2          
    c21 = p3 + p4           
    c22 = p1 + p5 - p3 - p7 '''
    q1 = products[0] + products[1]
    q2 = products[2] + products[3]
    q3 = products[4] + products[5]
    q4 = products[6] + products[7]
 
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((q1, q2)), np.hstack((q3, q4))))
 
    return c

if __name__ == "__main__":
    print("masukkan nilai n")
    n = int(input())
    A = np.random.randint(5, size=(n,n))
    B = np.random.randint(5, size=(n,n))
    C = []
    matrix_multiplication(A, B, C)
    print(C)
    with multiprocessing.Manager() as manager:
        products = manager.list([])
        start = time.time()
        C = hitung(A, B)
        stop = time.time()
        exec_time = stop - start
        print(f"execution time = {exec_time}")
        print(C)

    # t = []
    # for i in range(7):
    #     n = pangkat(2, i)
    #     A = np.random.randint(5, size=(n,n))
    #     B = np.random.randint(5, size=(n,n))
    #     print(A)
    #     print(B)
    #     start = time.time()
    #     C = strassen(A, B)
    #     stop =time.time()
    #     exec_time = stop - start
    #     print(C)
    #     print(f"execution time = {exec_time}")
    #     t.append(exec_time)
    # print(t)
