#coding:utf-8
'''
from multiprocessing import Pool
import time

def f(n):
    time.sleep(1)
    return n*n

if __name__=='__main__':
    a=range(10)
    p=Pool(5)
    print p.map(f,a)

from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    
    
    
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()

    print d
    print l

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"


from multiprocessing import Pool
import time
def f(x):
 #   print x*x
    time.sleep(1)
    return x*x
if __name__ == '__main__':
    p=Pool(processes=4)
    res_list=[]
    for i in range(10):
        res=p.apply_async(f,[i,])
        res_list.append(res)
        print "------" , i 
    for r in res_list:
        print r.get(timeout=1)

from multiprocessing import Manager,Process
def f(x,l):
    x['l']='p'
    l.reverse()

if __name__ == '__main__':
    m=Manager()
    x=m.dict()
    l=m.list(range(10))   
    p=Process(target=f,args=(x,l))
    p.start()
    p.join()
    print x
    print l
   
from multiprocessing import Manager,Process
def f(x,l):
    x['l']='p'
    l.reverse()
if __name__ == '__main__':   
    x={}
    l=range(10) 
    p=Process(target=f,args=(x,l))
    p.start()
    p.join()
    print x
    print l
 
from multiprocessing import Pool
import time
def f(x):
    time.sleep(2)
    return x*x
if __name__ == '__main__': 
    p=Pool(processes=5)
    x=range(10)
    res_list=[]
    for i in x:
        res=p.apply_async(f,[i,])
        res_list.append(res)
    for r in res_list:
        print r.get()
'''