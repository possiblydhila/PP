import multiprocessing
import numpy as np
import time
import os

def matrix_print(mA,mB,mC,mD,mE,mF,mG,mH):
    #print('pid0 = {}'.format(os.getpid()))
    print(f'A = {mA}')
    print(f'B = {mB}')
    print(f'C = {mC}')
    print(f'D = {mD}')
    print(f'E = {mE}')
    print(f'F = {mF}')
    print(f'G = {mG}')
    print(f'H = {mH}')

def matrix_multWXYZ(mA,mB,mC,mD,mE,mF,mG,mH, res):
    #print(f'pid1 = {os.getpid()}')
    W = mA @ mB 
    X = mC @ mD
    Y = mE @ mF
    Z = mG @ mH
    res.put((W,X,Y,Z))
    #print(f'W = {W}')
    #print(f'X = {X}')
    #print(f'Y = {Y}')
    #print(f'Z = {Z}')

def matrix_multMN(res):
    r = res.get()
    #print(f'pid2 = {os.getpid()}')
    M = r[0] @ r[1]
    N = r[2] @ r[3]
    res.put((M,N))
    #print(f'M = {M}')
    #print(f'N = {N}') 

def matrix_multFINAL(res):
    r = res.get()
    #print(f'pid3 = {os.getpid()}')
    fin = r[0] @ r[1]
    print(f'HASIL = {fin}')

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
    
    res = multiprocessing.Queue()
    #p0 = multiprocessing.Process(target=matrix_print, args=[A,B,C,D,E,F,G,H,])
    p1 = multiprocessing.Process(target=matrix_multWXYZ, args=[A,B,C,D,E,F,G,H,res])
    p2 = multiprocessing.Process(target=matrix_multMN, args=[res,])
    p3 = multiprocessing.Process(target=matrix_multFINAL, args=[res,])
    
    #p0.start()
    p1.start()
    p2.start()
    p3.start()

    #p0.join()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()
    print(f'time = {end-start}')