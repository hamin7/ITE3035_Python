from multiprocessing import Pool
import time
import os
import math

def f(x):
    # print("variable", x, "'s PID = ", os.getpid())
    return 3*x

def pid(x):
    return os.getpid()

if __name__ == '__main__':
    p = Pool(5)
    # startTime = int(time.time())
    print"Output of (1):"
    print
    print"output in order:", p.map(f, range(0,10))
    print
    time.sleep(1)
    # endTime = int(time.time())
    # print("Total work time", (endTime - startTime))
    print"Output of (3):"
    print
    print"PID:", p.map(pid, range(0,5))
    print
