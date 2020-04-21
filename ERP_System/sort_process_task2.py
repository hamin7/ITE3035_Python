import multiprocessing
import random
import timeit
import time

def sorting_thread(array, pid, lock) :
    
    print('############Thread #%d started...............\n' %pid)
    lock.acquire()
    start = timeit.default_timer()
    random_function(array)
    sorting_function(array)
    print_array(array, pid)
    stop = timeit.default_timer()
    print('%0.3f sec' %(stop-start))
    lock.release()
    
def random_function(array):
    i=0
    for i in range(10):
        array[i]=random.randrange(0,100)
    return    

def sorting_function(array) :
    i=9
    for i in range(9,0,-1):
        j=0
        for j in range(i):
            time.sleep(0.01)
            if array[j] > array[j+1] :
                tmp = array[j+1]
                array[j+1]=array[j]
                array[j]=tmp
    return            

def print_array(array, pid):
    print"[%d] --> "  %pid,;
    for i in range(10):
        print"%d " %array[i],;

if __name__ =='__main__' :
    array=multiprocessing.Array('i',[0]*10)
    print('############Start#############')
    lock = multiprocessing.Lock()
    for i in range(10) :
        p = multiprocessing.Process(target=sorting_thread, args=(array, i,lock))
        p.start()
    p.join()
    print('#############End###############')