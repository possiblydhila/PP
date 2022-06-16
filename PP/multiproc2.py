# sharing data antar process

import multiprocessing

def square_list(mylist, result, square_sum):
    for i, num in enumerate(mylist): 
        result[i] = num*num
    
    square_sum.value = sum(result)

    print("result in p1: {}".format(result[:]))
    print("sum of square in p1: {}".format(square_sum.value))

if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5]
    result = multiprocessing.Array('i',5) #tipe, jumlah array
    square_sum = multiprocessing.Value('i')
    p1 = multiprocessing.Process(target=square_list, args=[mylist, result, square_sum])
    p1.start()
    p1.join()

    print("result in main: {}".format(result[:]))
    print("sum of square in main: {}".format(square_sum.value))