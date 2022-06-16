#strassen parallel multiprocessing
import numpy as np
import multiprocessing
import time

def split(matrix): #fungsi bagi matriks. split = variabel
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
def proses(max1, max2, res):
     d = np.matmul(max1, max2)
     res.append(d)
      
def strassen(x, y):
    if len(x) == 1:
        return x * y
 
    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = multiprocessing.Process(target=proses, args=(a, f - h, result,))
    p2 = multiprocessing.Process(target=proses, args=(a + b, h, result,))       
    p3 = multiprocessing.Process(target=proses, args=(c + d, e, result,))   
    p4 = multiprocessing.Process(target=proses, args=(d, g - e, result,))       
    p5 = multiprocessing.Process(target=proses, args=(a + d, e + h, result,))         
    p6 = multiprocessing.Process(target=proses, args=(b-d, g+h, result,))
    p7 = multiprocessing.Process(target=proses, args=(a - c, e + f, result,))
 
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    # dibuat paralel
    c11 = result[4] + result[3] - result[1] + result[5] 
    c12 = result[0] + result[1]        
    c21 = result[2] + result[3]         
    c22 = result[0] + result[4] - result[2] - result[6]
 
    # menggabungkan hasil komponen 4 matriks yang udah diitung secara paralel
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    

    
if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
      result = manager.list([])
      
      print("masukkan nilai n")
      n = int(input())
      A = np.random.randint(5, size=(n,n))
      B = np.random.randint(5, size=(n,n))
      start = time.time()
      C = strassen(A, B)
      stop = time.time()
      exec_time = stop - start
      print(f"execution time = {exec_time}")