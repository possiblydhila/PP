# program hitung kubik & kuadrat dikerjakan dalam 2 processor yang berbeda

import multiprocessing
import os

def square(x: int):
    print("process id: {}".format(os.getpid()))
    print("square: {}".format(x*x))

def cube(x: int):
    print("process id: {}".format(os.getpid()))
    print("cube: {}".format(x*x*x))

if __name__ == "__main__":
    # process id main program
    print("main process id: {}".format(os.getpid()))
    # buat process
    p1 = multiprocessing.Process(target=square, args=[10,])
    p2 = multiprocessing.Process(target=cube, args=[10,])
    # start process
    p1.start()
    p2.start()
    # tunggu selesai
    p1.join()
    p2.join()

    print('done!')