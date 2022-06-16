import multiprocessing
import numpy as np
import time

A = np.random.randint(0, 5, size=(5, 5))
B = np.random.randint(0, 5, size=(5, 5))
C = np.random.randint(0, 5, size=(5, 5))
D = np.random.randint(0, 5, size=(5, 5))
E = np.random.randint(0, 5, size=(5, 5))
F = np.random.randint(0, 5, size=(5, 5))
G = np.random.randint(0, 5, size=(5, 5))
H = np.random.randint(0, 5, size=(5, 5))

   
def proses(max1, max2, res):
  compute = np.matmul(max1, max2)
  res.append(compute)
  

if __name__ == "__main__":
  with multiprocessing.Manager() as manager:
    start = time.time()
    server1 = manager.list([])
    pRes1 = multiprocessing.Process(target=proses, args=(A, B, server1, ))
    pRes2 = multiprocessing.Process(target=proses, args=(C, D, server1, ))
    
    server2 = manager.list([])
    pRes3 = multiprocessing.Process(target=proses, args=(E, F, server2, ))
    pRes4 = multiprocessing.Process(target=proses, args=(G, H, server2, ))
    
    pRes1.start()
    pRes2.start()
    pRes3.start()
    pRes4.start()

    pRes1.join()
    pRes2.join()
    pRes3.join()
    pRes4.join()

    server3 = manager.list([])
    pRes5 = multiprocessing.Process(target=proses, args=(server1[0], server1[1], server3, ))
    pRes6 = multiprocessing.Process(target=proses, args=(server2[0], server2[1], server3, ))
    
    pRes5.start()
    pRes6.start()
    pRes6.join()
    pRes5.join()
    
    result = manager.list([])
    res = multiprocessing.Process(target=proses, args=(server3[0], server3[1], result, ))
    res.start()
    res.join()
    
    end = time.time()
    print("Waktu eksekusi adalah:", end-start)
    print("Hasil matriks adalah:\n", result[0])

