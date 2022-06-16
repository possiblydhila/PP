import numpy as np
import time
import multiprocessing

def split(matrix):
    a = np.array(matrix)
    row, col = a.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
def multiply(A, B, res):
  for i in range(len(A)):
      col_C =[]
      for j in range(len(B[i])):
          x = 0
          for k in range(len(B)):
              x += A[i][k] * B[k][j]
          col_C.append(x)
      res.append(col_C)
  
def process(x, y):
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    
    p1 = multiprocessing.Process(target=multiply, args=(a, e, server)) 
    p2 = multiprocessing.Process(target=multiply, args=(b, g, server))       
    p3 = multiprocessing.Process(target=multiply, args=(a, f, server))       
    p4 = multiprocessing.Process(target=multiply, args=(b, h, server))
    p5 = multiprocessing.Process(target=multiply, args=(c, e, server))       
    p6 = multiprocessing.Process(target=multiply, args=(d, g, server)) 
    p7 = multiprocessing.Process(target=multiply, args=(c, f, server)) 
    p8 = multiprocessing.Process(target=multiply, args=(d, h, server)) 
    
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
    
    c11 = server[0] + server[1]
    c12 = server[2] + server[3]          
    c21 = server[4] + server[5]           
    c22 = server[6] + server[7]
    
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c

if _name_ == "_main_":
  with multiprocessing.Manager() as mp:
    server = mp.list([])
    print('insert n for n-by-n matrices A and B (matrix paralel)')
    n = int(input())
    A = np.random.randint(0, 9, size=(n, n))
    B = np.random.randint(0, 9, size=(n, n))
    print(A)
    print(B)
    start = time.time()
    C = process(A, B)
    print("Hasilnya :")
    print(C)
    stop = time.time()
    exec_time = stop - start
    print(f"execution time = {exec_time}")