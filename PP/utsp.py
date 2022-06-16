import numpy as np
import time
import threading

a = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [1, 1, 2, 6, 9],
              [7, 8, 9, 5, 4]])
  
b = np.array([[6, 2, 3, 3, 1],
              [4, 5, 6, 2, 7],
              [7, 8, 9, 5, 4],
              [7, 8, 9, 1, 2],
              [8, 1, 2, 1, 1]])

c = np.array([[7, 8, 9, 5, 4],
              [1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [1, 1, 2, 6, 9]])
  
d = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [7, 8, 9, 1, 2],
              [8, 1, 2, 1, 1]])

e = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [1, 1, 2, 6, 9],
              [7, 8, 9, 5, 4]])
  
f = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [7, 8, 9, 1, 2],
              [8, 1, 2, 1, 1]])

g = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 5, 4],
              [1, 1, 2, 6, 9],
              [7, 8, 9, 5, 4]])
  
h = np.array([[1, 2, 3, 3, 1],
              [4, 5, 6, 4, 7],
              [7, 8, 9, 1, 2],
              [8, 1, 2, 1, 1],
              [7, 8, 9, 5, 4]])


result =[]

def kali(a,b,c,d,e,f,g,h):
    res = np.array(a@b@c@d@e@f@g@h)
    print(res)

start = time.time()
if __name__ == "__main__":
    x = threading.Thread(target=kali, args=[a,b,c,d,e,f,g,h,])
    x.start()
    x.join()
    end = time.time()
    print(f'active threads: {threading.activeCount()}')
    print(f'time = {end-start}')


