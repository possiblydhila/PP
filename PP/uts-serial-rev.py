import numpy as np
import time

A = np.random.randint(10, size=(5,5))
B = np.random.randint(10, size=(5,5))
C = np.random.randint(10, size=(5,5))
D = np.random.randint(10, size=(5,5))
E = np.random.randint(10, size=(5,5))
F = np.random.randint(10, size=(5,5))
G = np.random.randint(10, size=(5,5))
H = np.random.randint(10, size=(5,5))

start = time.time()
if __name__ == "__main__":
    W = A @ B
    X = C @ D
    Y = E @ F
    Z = G @ H

    M = W @ X
    N = Y @ Z

    res = M @ N
    end = time.time()
    print(f'HASIL = {res}')
    print(f'time = {end-start}')