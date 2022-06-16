import threading
import time

def func():
    print('run')
    time.sleep(1)
    print('done')
    time.sleep(0.75)
    print('welldone')

def hitung(n, sleep_time):
    print('active threads:',threading.activeCount())
    for i in range(1, n+1):
        print(f"sleep_time: {sleep_time} count: {i}")
        time.sleep(sleep_time)

#generate thread untuk fungsi func
#x = threading.Thread(target=func) 
#x.start()
#active thread
#print(threading.activeCount())
#print('finally done')

for a in range(1,3):
    x = threading.Thread(target=hitung, args=[10, a,])
    x.start()
    
print('active threads:',threading.activeCount())
print('multithreading activated: ')