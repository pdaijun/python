#!/usr/bin/evn python
#coding:utf-8
'''
class Province(object):
    def __init__(self,name,capital,leader,fag):
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        self.__Thiand = fag
    def stemp_meet(self):
        print self.Name +'可以开运动会'
    @staticmethod
    def Foo():
        print '都是反腐'
    @property
    def Bar(self):
       #  print self.Name
        return 'something'
    
    def __sha(self):
        print 'daijun'
    
    def sha(self):
        return self.__sha()
    @property
    def shas(self):
        return self.__Thiand
    @shas.setter
    def shas(self,value):
        self.__Thiand=value

hb=Province('湖北','武汉','代军')
print hb.Capital
print hb.Name
print hb.Leader

hb=Province('湖北','武汉','代军') 
hb.stemp_meet()
Province.Foo()
hb.Foo() 
print hb.Bar

hb=Province('湖北','武汉','代军','True')
#hb.__Thiand
print hb.shas
hb.shas = 'flase'
print hb.shas
#print hb.sha()
#hb._Province__sha()

class Foo():
    def __init__(self):
        pass
    def __del__(self):
        print '退出了'
    def __call__(self):
        print 'FOO()'
f1 = Foo()
f1()
'''
class Test1():
    def __init__(self,name):
        self.__SHA=name
    @property
    def sha(self,value):
        self.__SHA=value
class Test2(object):
    def __init__(self,name):
        self.__SHA=name
    @property
    def sha(self):
        return self.__SHA
    @sha.setter
    def sha(self,value):
        self.__SHA=value
T1=Test1('daijun')
T1.sha='peng'
print T1.sha
T2=Test2('daijun')
T2.sha='peng'
print T2.sha