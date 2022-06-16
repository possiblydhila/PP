import threading
import numpy as np
import time

def matrix_mult(mA,mB,mC,mD,mE,mF,mG,mH):
    Y = mA @ mB @ mC @ mD @ mE @ mF @ mG @ mH
    print('Y = {}'.format(Y))

start = time.time()
if __name__ == "__main__":
    A = np.random.randint(10, size=(5,5))
    B = np.random.randint(10, size=(5,5))
    C = np.random.randint(10, size=(5,5))
    D = np.random.randint(10, size=(5,5))
    E = np.random.randint(10, size=(5,5))
    F = np.random.randint(10, size=(5,5))
    G = np.random.randint(10, size=(5,5))
    H = np.random.randint(10, size=(5,5))
    print('A = {}'.format(A))
    print('B = {}'.format(B))
    print('C = {}'.format(C))
    print('D = {}'.format(D))
    print('E = {}'.format(E))
    print('F = {}'.format(F))
    print('G = {}'.format(G))
    print('H = {}'.format(H))
    
    t1 = threading.Thread(target=matrix_mult, args=[A,B,C,D,E,F,G,H,])
    t1.start()
    t1.join()
    end = time.time()
    print(f'time = {end-start}')