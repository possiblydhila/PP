import queue
import time
import threading
input_value = [1,2,5,4,3,7,6]
my_queue = queue.Queue()
# Process
def multiply(x):
    output_value = []
    for i in range(1, x+1):
        output_value.append(i*x)
    time.sleep(2)
    print(f"output({x}) = {output_value}")

# Process queue
def process_queue():
    while True:
        try:
            value = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            #multiply(value)
            # Multithreading
            x = threading.Thread(target=multiply, args=[value,])
            x.start()
# Fill queue
for x in input_value:
    my_queue.put(x)

process_queue()