from multiprocessing import Pool
import time
import os
import math

def f(x):
    # print("variable", x, "'s PID = ", os.getpid())
    time.sleep(1)
    return 3*x

if __name__ == '__main__':
    p = Pool(5)
    startTime = int(time.time())
    print"output in order:",p.map(f, range(0,10))
    endTime = int(time.time())
    print("Total work time", (endTime - startTime))
