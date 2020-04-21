from multiprocessing import Pool

def calc(a,b):
    return a*b+1

if __name__ == '__main__':
    with Pool(processes=16) as p:
        res = [p.apply_async(calc, args=(i,2)) for i in range(20)]
        result = [r.get() for r in res]
        print(result)
