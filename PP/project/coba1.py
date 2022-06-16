import threading
import time

def task1(): 
    print('send first email')
    time.sleep(5) 
    print('first email reply')

def task2():
    print('send second email')
    time.sleep(2)
    print('second email reply')

def task3():
    print('send third email')
    time.sleep(1)
    print('third email reply')

def main():
    x = threading.Thread(target=task1)
    y = threading.Thread(target=task2)
    z = threading.Thread(target=task3)
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('active threads:', threading.activeCount())
    print(f"{end-start} seconds")

