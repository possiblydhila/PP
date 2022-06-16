import multiprocessing
import numpy as np
import time
import os

def matrix_print(mA,mB,mC,mD,mE,mF,mG,mH):
    print('pid = {}'.format(os.getpid()))
    print('A = {}'.format(mA))
    print('B = {}'.format(mB))
    print('C = {}'.format(mC))
    print('D = {}'.format(mD))
    print('E = {}'.format(mE))
    print('F = {}'.format(mF))
    print('G = {}'.format(mG))
    print('H = {}'.format(mH))

def matrix_mult(mA,mB,mC,mD,mE,mF,mG,mH):
    print('pid = {}'.format(os.getpid()))
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

    #p1 = multiprocessing.Process(target=matrix_print, args=[A,B,C,D,E,F,G,H])
    p2 = multiprocessing.Process(target=matrix_mult, args=[A,B,C,D,E,F,G,H,])
    #p1.start()
    p2.start()
    #p1.join()
    p2.join()
    end = time.time()
    print(f'time = {end-start}')