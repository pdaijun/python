#conding:utf-8
'''
temp=(lambda x,y:x+y)
print temp(4,4)


x=map(lambda x:x*2 , range(10))
print x

a=[]
print dir(a) 
print vars(a)
type(a)      


from file import demo

demo.foo()

print divmod(9,4)
print bool(1)
print pow(2,10)

li=[10,11,111]
def foo(arg):
    return arg +100
#x=map(foo,li)
#print x
x=map(lambda arg:arg+100,li)
print x

from test.test_support import temp_cwd
li=[10,11,111]
def foo(arg):
    if arg >20:
        return True
    else:
        return False
temp = filter(foo,li) 
print temp

li=[10,11,111]
print reduce(lambda x,y:x*y, li)

x=[1,2,3,4]
y=[2,3,5,1]
z=[7,8,9]
d=[2,4,5,8,8]
n=zip(x,y,z,d)
print n[0],n[1],n[2]

import random
code=[]
for i in range(6):
    if i==random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp=random.randint(65,90)
        code.append(chr(temp))
x=''.join(code)
print x

print ord('Z')

from test.badsyntax_future3 import result

import pickle
li=['daijun','is','good']
ser_li= pickle.dumps(li)
print ser_li
li2 = pickle.loads(ser_li)
print li2

import pickle
li={'name':'daijun','age':18}
pickle.dump(li, open('C:/Users/dpeng/Desktop/RXR.pk','w'))
result=pickle.load(open('C:/Users/dpeng/Desktop/RXR.pk','r'))
print result

import json
li={'name':'daijun','age':18}
ser_li= json.dumps(li)
result = json.loads(ser_li)
print result

import json
li={'name':'daijun','age':18}
json.dump(li,open('C:/Users/dpeng/Desktop/RER.json','w'))
result = json.load(open('C:/Users/dpeng/Desktop/RER.json','r'))
print result
'''
