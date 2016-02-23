#coding:utf-8
'''
import time
from Queue import Queue
from threading import Thread

def Foo():
    for item in range(100):
        print item
        time.sleep(1)    
print 'before'
t1= Thread(target=Foo)
t1.setDaemon(True)
t1.start()
print t1.isDaemon()

print t1.getName()

t2= Thread(target=Foo,args=(22222,))
t2.start()
print t2.getName()

print 'after'
print 'after'
print 'after'
print 'after'
print 'after'
print 'after'
#time.sleep(10)




import os

input =raw_input('path:')
print input
cmd,pathx = input.split('|')
print cmd 
print pathx
print type(pathx)

path=str('C:\Users\dpeng\workspace\day6\\third\demo\index.py')
print path
print type(path)
x=os.path.basename(path)
z=os.stat(path)
y=os.stat(path).st_size
print x
print z
print y

import time
from Queue import Queue
from threading import Thread


class Product(Thread):
    
    def __init__(self,target,queue):
        self.__target=target
        self.__queue=queue
        super(Product,self).__init__()
    
    def run(self):
        while True: 
            if self.__queue.full():                
                time.sleep(1)
            else:
                self.__queue.put('包子')
                
                print '生产一个包子'
                time.sleep(1)
class Comsumer(Thread):
    
    def __init__(self,target,queue):
        self.__target=target
        self.__queue=queue
        super(Comsumer,self).__init__()
    
    def run(self):
        while True: 
            if self.__queue.empty():                
                time.sleep(1)
            else:
                self.__queue.get()
                print '消费一个包子'
                time.sleep(1)
que = Queue(maxsize=100)
daijun1= Product('daijun1',que)
daijun1.start()
daijun2= Product('daijun2',que)
daijun2.start()
daijun3= Product('daijun3',que)
daijun3.start()
for item in range(20):
    name = 'peng%d' %(item,)
    temp = Comsumer(name,que)
    temp.start()


import time 
import threading
num = 0
num1 = 100
def run():  
  
    time.sleep(1)
    global num
    global num1
    lock.acquire()
    num +=1
    lock.acquire()
    num +=1
    lock.release()
    lock.release()
    time.sleep(0.01)
    print '%s' % num
     
lock=threading.BoundedSemaphore()
for items in range(100):
    t=threading.Thread(target=run)
    t.start()
'''
import threading,time

def product():
    print '卖包子咯，新鲜的包子！'
    event.wait()
    event.clear()
    print"peng:daijun来买包子了"
    print "peng:为daijun做包子"
    time.sleep(10)
    print "peng:你的包子好了"
    event.set()

def comsumer():
    print "daijun:去买包子"                                   
    event.set()
    time.sleep(1)
    print "包子做好"
    event.wait()
    print 'Thanks...'
'''    while True:
        if  event.is_set():
            print 'Thanks...'
            break
        else:
            print "怎么还没做好啊!!!" 
            time.sleep(1)           
'''
event=threading.Event()               
t1=threading.Thread(target=product)
t2=threading.Thread(target=comsumer)
t2.start()
t1.start()               
                
                
                
                
                
                
                
                
                
                
                
                