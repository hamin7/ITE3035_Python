from multiprocessing import Pool
import time
import os
import random

def f(x):
    return 3*x

def pid(x):
    return os.getpid()

if __name__ == '__main__':
    p = Pool(5)
    
    print"Output of (1):"
    print
    print"Output in order:", p.map(f, range(0,10))
    print

    time.sleep(5)

    print"Output of (2):"
    print
    sampleList = p.map(f, range(0,10)) 
    print random.sample(sampleList, 10)
    print

    time.sleep(5)

    print"Output of (3):"
    print
    print"PID:", p.map(pid, range(0,5))
    print
