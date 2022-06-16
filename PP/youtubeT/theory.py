# GENERATORS = produces a sequence of values

# Produce a sequence of odd values
def odds(start, stop):
    for odd in range(start, stop + 1):
        yield odd

def main():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)

if __name__ == "__main__":
    main()

'''
synchronous = doing things sequencialy
COROUTINES = wrapped version of a function that allows it to run asynchronously. 
generealize subroutines for non-premptive multitasking, by allowing execution 
to be suspended/resumed

'''