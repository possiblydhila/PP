import multiprocessing
import numpy as np
import time
import os

def matrix_print(mA,mB,mC,mD,mE,mF,mG,mH):
    print('A = {}'.format(mA))
    print('B = {}'.format(mB))
    print('C = {}'.format(mC))
    print('D = {}'.format(mD))
    print('E = {}'.format(mE))
    print('F = {}'.format(mF))
    print('G = {}'.format(mG))
    print('H = {}'.format(mH))

def process1(mA,mB,mC,mD,mE,mF,mG,mH,q):
    t1 = mA @ mB
    t2 = mC @ mD
    t3 = mE @ mF
    t4 = mG @ mH
    q.put((t1,t2,t3,t4))
    print('T1 = {}'.format(t1))
    print('T2 = {}'.format(t2))
    print('T3 = {}'.format(t3))
    print('T4 = {}'.format(t4))
    
def process2(q):
    result = q.get()
    t12 = result[0] @ result[1]
    t34 = result[2] @ result[3]
    print('T12 = {}'.format(t12))
    print('T34 = {}'.format(t34))
    q.put((t12,t34))

def process3(q):
    result = q.get()
    Y = result[0] @ result[1]
    print('Y = {}'.format(Y))
    
    
start = time.time()
if _name_ == "_main_":
    size = 5
    A = np.random.randint(10, size=(size,size))
    B = np.random.randint(10, size=(size,size))
    C = np.random.randint(10, size=(size,size))
    D = np.random.randint(10, size=(size,size))
    E = np.random.randint(10, size=(size,size))
    F = np.random.randint(10, size=(size,size))
    G = np.random.randint(10, size=(size,size))
    H = np.random.randint(10, size=(size,size))
    q = multiprocessing.Queue()
    matrix_print(A,B,C,D,E,F,G,H)
    p1 = multiprocessing.Process(target=process1, args=(A,B,C,D,E,F,G,H,q))
    p2 = multiprocessing.Process(target=process2, args=(q,))
    p3 = multiprocessing.Process(target=process3, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    end = time.time()
    print(f'time = {end-start}')